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
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'])
    extend_([u'    <title>Crosswynds Traders</title>\n'])
    extend_([u'    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">\n'])
    extend_([u'    <link rel="stylesheet" href="/static/styles/promo.css">\n'])
    extend_([u'    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n'])
    extend_([u'    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>\n'])
    extend_([u'    <script src="/static/scripts/promo.js"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="contentContainer" class="container-fluid">\n'])
    extend_([u'        <!-- Create the Main Content layout.-->\n'])
    extend_([u'        <!-- Get the Main Content from the server -->\n'])
    extend_([u'        ', escape_(page, False), u'\n'])
    extend_([u'        <!-- Ends Main Content Layout -->\n'])
    extend_([u'    </div>\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def new (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="comingSoonHeader" class="col-lg-12 jumbotron comingsoon-jumbotron">\n'])
    extend_([u'        <!-- Header Image -->\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="signUpArea" class="col-sm-6">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h3>Sign up early and earn rewards</h3>\n'])
    extend_([u'                <form method="POST">\n'])
    extend_([u'                    ', escape_(form.render_css(), False), u'\n'])
    extend_([u'                </form>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

new = CompiledTemplate(new, 'templates/new.html')
join_ = new._join; escape_ = new._escape

# coding: utf-8
def privacy():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

    return self

privacy = CompiledTemplate(privacy, 'templates/privacy.html')
join_ = privacy._join; escape_ = privacy._escape

# coding: utf-8
def refer():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'hello REFERAL world\n'])

    return self

refer = CompiledTemplate(refer, 'templates/refer.html')
join_ = refer._join; escape_ = refer._escape

