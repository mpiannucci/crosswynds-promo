from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def admin():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'You are admin\n'])

    return self

admin = CompiledTemplate(admin, 'templates/admin.html')
join_ = admin._join; escape_ = admin._escape

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
    extend_([u'        <!-- Sign Up Form -->\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u"            <h1>Don't Get Left Behind at the Beach!</h1>\n"])
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
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="privacyTitle" class="col-sm-12 jumbotron">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1>Privacy Policy</h1>\n'])
    extend_([u'            <p>Crosswynds Traders</p>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="col-sm-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <p>At Crosswynds Traders we take your privacy very seriously. The only personal information we collect on this site is your email address and your IP Address. All information you provide is kept in strict confidence and will never be sold or given to a third party for any reason.</p>\n'])
    extend_([u'\n'])
    extend_([u'            <h3>Disclaimer</h3>\n'])
    extend_([u'\n'])
    extend_([u'            <p>The owner of this website will not be held liable for the misuse of this site or any site which is linked to by people who are not authorized to distribute email addresses, or perform any other type of action.</p>\n'])
    extend_([u'\n'])
    extend_([u'            <p>It is the intention of Crosswynds Traders and its associates to provide accurate information, but neither the owner of Crosswynds Traders nor its associates claims any responsibility for any inaccurate information provided in error.</p>\n'])
    extend_([u'\n'])
    extend_([u'            <p>All items on this site are advertised for promotional value only. The actual appearence or usefulness of rewards earned on this site may not meet your expectations. </p>\n'])
    extend_([u'\n'])
    extend_([u"            <p>It is the user of this site's responsibility to be aware of and abide by all laws in accordance to their geographical location or jurisdiction. Crosswynds Traders will not be held liable for any claims that damages caused to a person or any type of hardware or software were caused by the use of this site or any partner sites.</p>\n"])
    extend_([u'\n'])
    extend_([u'            <h3>Contact</h3>\n'])
    extend_([u'            <p>Crosswynds Traders<br>\n'])
    extend_([u'            1175 Boston Neck Rd<br>\n'])
    extend_([u'            Narragansett, RI 02882<br>\n'])
    extend_([u'            (401) 782-1110</p>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

privacy = CompiledTemplate(privacy, 'templates/privacy.html')
join_ = privacy._join; escape_ = privacy._escape

# coding: utf-8
def refer (count, ref_url):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="confimationHeader" class="col-lg-12 confirmation-header">\n'])
    extend_([u'        <!-- Header bar -->\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h4>Thanks for signing up!</h4>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="sharingImage" class="col-lg-12 sharing-jumbotron">\n'])
    extend_([u'        <!-- Large Sharing image -->\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="sharingArea" class="col-lg-12 center-align">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <div class="col-sm-12">\n'])
    extend_([u'                <h3>Share your unique link with your friends to earn rewards!</h3>\n'])
    extend_([u'                <h4>The more of your friends join, the more free merchandise you earn.</h4>\n'])
    extend_([u'            </div>\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Referral URL -->\n'])
    extend_([u'            <div class="col-sm-4 col-sm-offset-3 center-align">\n'])
    extend_([u'                <input id="referral_display" class="form-control input ref-url-display default-cursor hvr-grow" type="text" value=\'', escape_(ref_url, True), u'\' onclick="onReferralURLClick()" readonly="readonly">\n'])
    extend_([u'            </div>\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Facebook Link -->\n'])
    extend_([u'            <div class="col-sm-1">\n'])
    extend_([u'                <a class="hvr-grow" href="http://www.facebook.com/sharer/sharer.php?u=', escape_(ref_url, True), u'&title=Crosswynds">\n'])
    extend_([u'                    <img class="social-logo" src="/static/images/facebook_logo.png" />\n'])
    extend_([u'                </a>\n'])
    extend_([u'            </div>\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Twitter Link -->                  \n'])
    extend_([u'            <div class="col-sm-1">\n'])
    extend_([u'                <a class="hvr-grow" href="http://twitter.com/share?url=', escape_(ref_url, True), u'&text=I+can\'t+wait+for Crosswynds+online+store+to+launch!+Im+gunna+be+hitting+the+beach+in+style">\n'])
    extend_([u'                    <img class="social-logo" src="/static/images/twitter_logo.png" />\n'])
    extend_([u'                </a>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="scoreArea" class="col-lg-12 center-align">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Friend Referral Score -->\n'])
    extend_([u'            <h3>', escape_(count, True), u' of your friends have joined!</h3>\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Reward Pictures -->\n'])
    extend_([u'            <div class="row">\n'])
    extend_([u'                <div class="col-sm-3">  \n'])
    if count >= 5:
        extend_(['                    ', u'<img class="reward-image img-circle hvr-grow" src="/static/images/five_friends.png">\n'])
    else:
        extend_(['                    ', u'<img class="reward-image img-circle img-bw hvr-grow" src="/static/images/five_friends.png">                \n'])
    extend_([u'                    <h4>5 Friends</h4>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div class="col-sm-3">\n'])
    if count >= 10:
        extend_(['                    ', u'<img class="reward-image img-circle hvr-grow" src="/static/images/ten_friends.png">\n'])
    else:
        extend_(['                    ', u'<img class="reward-image img-circle img-bw hvr-grow" src="/static/images/ten_friends.png">\n'])
    extend_([u'                    <h4>10 Friends</h4>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div class="col-sm-3">\n'])
    if count >=25:
        extend_(['                    ', u'<img class="reward-image img-circle hvr-grow" src="/static/images/twentyfive_friends.png">\n'])
    else:
        extend_(['                    ', u'<img class="reward-image img-circle img-bw hvr-grow" src="/static/images/twentyfive_friends.png">\n'])
    extend_([u'                    <h4>25 Friends</h4>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div class="col-sm-3">\n'])
    if count >=50:
        extend_(['                    ', u'<img class="reward-image img-circle hvr-grow" src="/static/images/spirit_jersey.png">\n'])
    else:
        extend_(['                    ', u'<img class="reward-image img-circle img-bw hvr-grow" src="/static/images/spirit_jersey.png">\n'])
    extend_([u'                    <h4>50 Friends</h4>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'\n'])
    extend_([u'            <!-- Rewards Progress Bar -->\n'])
    extend_([u'            <div class="progress">\n'])
    extend_([u'\n'])
    extend_([u'                <!-- First Reward -->\n'])
    firstRewardPercent = 0
    if count > 5:
        firstRewardPercent = 25
    else:
        firstRewardPercent = count * 5
    if firstRewardPercent < 25:
        extend_(['                ', u'<div class="progress-bar progress-bar-almost" role="progressbar" style="width:', escape_(firstRewardPercent, True), u'%">\n'])
    else:
        extend_(['                ', u'<div class="progress-bar progress-bar-salmon" role="progressbar" style="width:', escape_(firstRewardPercent, True), u'%">\n'])
        extend_(['                ', u'$', u'10 Off Coupon\n'])
    extend_([u'                </div>\n'])
    extend_([u'\n'])
    extend_([u'                <!-- Second Reward -->\n'])
    secondRewardPercent = 0
    if count > 5:
        if count > 10:
            secondRewardPercent = 25
        else:
            secondRewardPercent = (count - 5) * 5
        if secondRewardPercent < 25:
            extend_(['                ', u'<div class="progress-bar progress-bar-almost" role="progressbar" style="width:', escape_(secondRewardPercent, True), u'%">\n'])
        else:
            extend_(['                ', u'<div class="progress-bar progress-bar-purple" role="progressbar" style="width:', escape_(secondRewardPercent, True), u'%">\n'])
            extend_(['                ', u'$', u'20 Off Coupon\n'])
        extend_(['                ', u'</div>\n'])
        extend_(['                ', u'\n'])
    extend_([u'                <!-- Third Reward -->\n'])
    thirdRewardPercent = 0
    if count > 10:
        if count > 25:
            thirdRewardPercent = 25
        else:
            thirdRewardPercent = (count - 10) * (25/15.0)
        if thirdRewardPercent < 25:
            extend_(['                ', u'<div class="progress-bar progress-bar-almost" role="progressbar" style="width:', escape_(thirdRewardPercent, True), u'%">\n'])
        else:
            extend_(['                ', u'<div class="progress-bar progress-bar-blue" role="progressbar" style="width:', escape_(thirdRewardPercent, True), u'%">\n'])
            extend_(['                ', u'$', u'50 Off Coupon\n'])
        extend_(['                ', u'</div>\n'])
        extend_(['                ', u'\n'])
    extend_([u'                <!-- Fourth Reward -->\n'])
    fourthRewardPercent = 0
    if count > 25:
        if count > 50:
            fourthRewardPercent = 25
        else:
            fourthRewardPercent = count - 25
        if fourthRewardPercent < 25:
            extend_(['                ', u'<div class="progress-bar progress-bar-almost" role="progressbar" style="width:', escape_(fourthRewardPercent, True), u'%">\n'])
        else:
            extend_(['                ', u'<div class="progress-bar progress-bar-green" role="progressbar" style="width:', escape_(fourthRewardPercent, True), u'%">\n'])
            extend_(['                ', u'Free Spirit Jersey\n'])
        extend_(['                ', u'</div>\n'])
        extend_(['                ', u'\n'])
    extend_([u'                <!-- If nothing has been earned -->\n'])
    if count < 1:
        extend_(['                ', u'<div class="progress-bar progress-bar-almost" role="progressbar" style="width:100%">\n'])
        extend_(['                ', u"    You haven't earned any points yet.. Check back soon!\n"])
        extend_(['                ', u'</div>\n'])
        extend_(['                ', u'\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="referFooter" class="col-sm-12 center-align">\n'])
    extend_([u'        <a href="/privacy">Privacy Policy</a>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

refer = CompiledTemplate(refer, 'templates/refer.html')
join_ = refer._join; escape_ = refer._escape

