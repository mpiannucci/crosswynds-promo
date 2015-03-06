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
def ip_block():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'Too many attempts from your computer\n'])

    return self

ip_block = CompiledTemplate(ip_block, 'templates/ip_block.html')
join_ = ip_block._join; escape_ = ip_block._escape

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
    extend_([u'Privacyyyyy\n'])

    return self

privacy = CompiledTemplate(privacy, 'templates/privacy.html')
join_ = privacy._join; escape_ = privacy._escape

# coding: utf-8
def refer (count):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="confimationHeader" class="col-lg-12 confirmation-header">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h4>Thanks for signing up!</h4>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="sharingImage" class="col-lg-12 sharing-jumbotron">\n'])
    extend_([u'        <!-- Large Sharing image -->\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="sharingArea" class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <div class="col-sm-12">\n'])
    extend_([u'                <h2>Share your unique link with your friends to earn rewards!</h2>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-sm-3 col-sm-offset-3 social-logo">\n'])
    extend_([u'                <a href="http://www.facebook.com/sharer/sharer.php?u=http://mpiannucci.com/apps&title=Matthew">\n'])
    extend_([u'                    <img style="max-height:220px" src="/static/images/facebook_logo.png" />\n'])
    extend_([u'                </a>\n'])
    extend_([u'            </div>                       \n'])
    extend_([u'            <div class="col-sm-3 social-logo">\n'])
    extend_([u'                <a href="http://twitter.com/share?url=http://mpiannucci.com/apps&text=Imhappy">\n'])
    extend_([u'                    <img style="max-height:220px" src="/static/images/twitter_logo.png" />\n'])
    extend_([u'                </a>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-sm-12">\n'])
    extend_([u'                <h4>The more of your friends join, the more free merchandise you earn.</h4>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="scoreArea" class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h3>', escape_(count, True), u' of your friends have joined!</h3>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

refer = CompiledTemplate(refer, 'templates/refer.html')
join_ = refer._join; escape_ = refer._escape

