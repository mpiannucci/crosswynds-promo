from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n'])
    extend_([u'    <title>Crosswynds Traders</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
    extend_([u'\n'])
    extend_([u'<!-- TODO: Make the boilerplate base template -->\n'])
    extend_([escape_(page, False), u'\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

