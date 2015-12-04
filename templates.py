"""
 This is adapted from https://github.com/alexmic/microtemplates
 Updated for python 3
 Added iterative variable replacement, and choices for variable values.
 Removed calls, ifs, and lists
"""

__author__ = "Matt Fister"

import re
import operator
import ast
import random

VAR_FRAGMENT = 0
TEXT_FRAGMENT = 2

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'


TOK_REGEX = re.compile(r"(%s.*?%s)" % (
    VAR_TOKEN_START,
    VAR_TOKEN_END,
))

WHITESPACE = re.compile('\s+')


class TemplateError(Exception):
    pass


class TemplateContextError(TemplateError):

    def __init__(self, context_var):
        self.context_var = context_var

    def __str__(self):
        return "cannot resolve '%s'" % self.context_var


class TemplateSyntaxError(TemplateError):

    def __init__(self, error_syntax):
        self.error_syntax = error_syntax

    def __str__(self):
        return "'%s' seems like invalid syntax" % self.error_syntax


def eval_expression(expr):
    try:
        return 'literal', ast.literal_eval(expr)
    except ValueError:
        return 'name', expr
    except SyntaxError:
        return 'name', expr


def resolve(name, context):
    if name.startswith('..'):
        context = context.get('..', {})
        name = name[2:]
    try:
        for tok in name.split('.'):
            context = context[tok]
        return context
    except KeyError:
        raise TemplateContextError(name)


class _Fragment(object):
    def __init__(self, raw_text):
        self.raw = raw_text
        self.clean = self.clean_fragment()

    def clean_fragment(self):
        if self.raw[:2] in (VAR_TOKEN_START):
            return self.raw.strip()[2:-2].strip()
        return self.raw

    @property
    def type(self):
        raw_start = self.raw[:2]
        if raw_start == VAR_TOKEN_START:
            return VAR_FRAGMENT
        else:
            return TEXT_FRAGMENT


class _Node(object):
    creates_scope = False

    def __init__(self, fragment=None):
        self.children = []
        self.process_fragment(fragment)

    def process_fragment(self, fragment):
        pass

    def enter_scope(self):
        pass

    def render(self, context):
        pass

    def exit_scope(self):
        pass

    def render_children(self, context, children=None):
        if children is None:
            children = self.children
        def render_child(child):
            child_html = child.render(context)
            return '' if not child_html else str(child_html)
        return ''.join(map(render_child, children))


class _ScopableNode(_Node):
    creates_scope = True


class _Root(_Node):
    def render(self, context):
        return self.render_children(context)


class _Variable(_Node):
    def process_fragment(self, fragment):
        self.name = fragment

    def render(self, context):
        return resolve(self.name, context)


class _Text(_Node):
    def process_fragment(self, fragment):
        self.text = fragment

    def render(self, context):
        return self.text


class Compiler(object):
    def __init__(self, template_string):
        self.template_string = template_string

    def each_fragment(self):
        for fragment in TOK_REGEX.split(self.template_string):
            if fragment:
                yield _Fragment(fragment)

    def compile(self):
        root = _Root()
        scope_stack = [root]
        for fragment in self.each_fragment():
            if not scope_stack:
                raise TemplateError('nesting issues')
            parent_scope = scope_stack[-1]
            new_node = self.create_node(fragment)
            if new_node:
                parent_scope.children.append(new_node)
                if new_node.creates_scope:
                    scope_stack.append(new_node)
                    new_node.enter_scope()
        return root

    def create_node(self, fragment):
        node_class = None
        if fragment.type == TEXT_FRAGMENT:
            node_class = _Text
        elif fragment.type == VAR_FRAGMENT:
            node_class = _Variable
        if node_class is None:
            raise TemplateSyntaxError(fragment)
        return node_class(fragment.clean)


class Template(object):
    def __init__(self, contents):
        self.contents = contents
        self.root = Compiler(contents).compile()

    def render(self, **kwargs):
        new_kwargs = {}
        for key, val in kwargs.items():
            if isinstance(val, (str)):
                print(key + " " + val)
                parts = val.split('|')
                part_choice = random.choice(parts)
                new_kwargs[key] = part_choice
            else:
                print(key + " " + str(val))
                part_choice = random.choice(val)
                new_kwargs[key] = part_choice
        while VAR_TOKEN_START in self.contents:
            self.contents = self.root.render(new_kwargs)
            self.root = Compiler(self.contents).compile()
        return self.contents

if __name__ == '__main__':
    context = {'greeting': ['bonjour'.title(), 'hello'.title(), 'yo'.title()], 'world': '{{adjective}} world',
               'adjective': '{{sad word}}|{{happy word}}',
               'sad word': 'crappy|sad', 'happy word': 'joyful|crazy|wonderful'}
    print(Template("{{greeting}} {{world}}").render(**context))
