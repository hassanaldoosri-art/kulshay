# Builds the public pages for «كل شي» (support, privacy policy, terms) into ./docs for GitHub Pages.
# Usage: python build.py <support-email>
import io
import os
import sys

EMAIL = sys.argv[1]
UPDATED_AR, UPDATED_EN = '16 نوفمبر 2026', '16 November 2026'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Tajawal',system-ui,-apple-system,'Segoe UI',Tahoma,sans-serif;color:#13294B;background:#F6F7F9;line-height:1.8;font-size:17px}
header{background:#13294B;color:#fff;padding:22px 20px}
.bar{max-width:820px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:12px;color:#fff;text-decoration:none;font-weight:700;font-size:22px}
.brand svg{width:42px;height:42px}
nav{display:flex;gap:18px;flex-wrap:wrap}
nav a{color:#B8C2D3;text-decoration:none;font-size:15px}
nav a.on,nav a:hover{color:#fff}
main{max-width:820px;margin:0 auto;padding:28px 20px 60px}
section{background:#fff;border-radius:18px;padding:26px 24px;margin-bottom:22px}
h1{font-size:28px;line-height:1.4;margin-bottom:4px}
h2{font-size:19px;margin:22px 0 6px}
p,li{color:#3A465C}
ul{padding-inline-start:22px;margin:6px 0}
.muted{color:#8A94A6;font-size:14px}
a{color:#D95B12}
.btn{display:inline-block;background:#F26B1D;color:#fff;text-decoration:none;font-weight:700;border-radius:14px;padding:12px 22px;margin-top:10px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
.cards a{display:block;background:#F6F7F9;border-radius:14px;padding:16px;text-decoration:none;color:#13294B;font-weight:700}
.cards a span{display:block;font-weight:400;color:#5B667A;font-size:14px}
footer{text-align:center;color:#8A94A6;font-size:14px;padding:0 20px 40px}
[dir=ltr]{text-align:left}
"""

LOGO = '<svg viewBox="0 0 120 120"><rect x="4" y="4" width="112" height="112" rx="28" fill="#1E3A66"/><path d="M84 28 V88 H36 V72" fill="none" stroke="#F26B1D" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/><path d="M46 38 L62 46 L50 54 L66 62" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

NAV = [('index.html', 'الرئيسية'), ('support.html', 'الدعم'), ('privacy.html', 'الخصوصية'), ('terms.html', 'الشروط')]


def page(filename, title, body):
    nav = ''.join('<a href="%s"%s>%s</a>' % (f, ' class="on"' if f == filename else '', t) for f, t in NAV)
    html = """<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s · كل شي</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header><div class="bar"><a class="brand" href="index.html">%s كل شي</a><nav>%s</nav></div></header>
<main>
%s
</main>
<footer>© 2026 كل شي · Kul Shay</footer>
</body>
</html>
""" % (title, CSS, LOGO, nav, body)
    io.open(os.path.join('docs', filename), 'w', encoding='utf-8', newline='\n').write(html.replace('{{EMAIL}}', EMAIL))


os.makedirs('docs', exist_ok=True)
MAIL = '<a href="mailto:{{EMAIL}}" dir="ltr">{{EMAIL}}</a>'

# ---------------------------------------------------------------- home
page('index.html', 'صيانة منزلية', """
<section>
  <h1>كل شي لبيتك في مكان واحد</h1>
  <p>«كل شي» تطبيق سعودي يوصّلك بفني صيانة قريب منك وموثوق: سباكة، كهرباء، تكييف، أجهزة منزلية، نجارة، دهان، تنظيف، مكافحة حشرات، نقل عفش وغيرها.</p>
  <p>صوّر المشكلة، حدد الوقت، واختر من الفنيين اللي قبلوا طلبك. وكل شغل مضمون 30 يوم.</p>
  <div class="cards">
    <a href="support.html">الدعم والمساعدة<span>أسئلة شائعة وطريقة التواصل</span></a>
    <a href="privacy.html">سياسة الخصوصية<span>وش البيانات اللي نجمعها وكيف نستخدمها</span></a>
    <a href="terms.html">الشروط والأحكام<span>قواعد استخدام التطبيق</span></a>
  </div>
</section>
<section dir="ltr" lang="en">
  <h1>Kul Shay</h1>
  <p>A Saudi home-maintenance app that connects you with a trusted technician near you: plumbing, electrical, air conditioning, appliances, carpentry, painting, cleaning, pest control, moving and more. Every job carries a 30-day warranty.</p>
  <p><a href="support.html">Support</a> · <a href="privacy.html">Privacy policy</a> · <a href="terms.html">Terms of use</a></p>
</section>
""")

# ---------------------------------------------------------------- support
page('support.html', 'الدعم والمساعدة', """
<section>
  <h1>الدعم والمساعدة</h1>
  <p>عندك سؤال أو مشكلة في طلب؟ راسلنا ونرد عليك في أقرب وقت.</p>
  <a class="btn" href="mailto:{{EMAIL}}">راسلنا على الإيميل</a>
  <p class="muted" style="margin-top:10px">الإيميل: %(mail)s. اكتب رقم الطلب ورقم جوالك المسجّل عشان نخدمك أسرع.</p>

  <h2>كيف أطلب فني؟</h2>
  <p>اختر الخدمة، صوّر المشكلة أو اكتب وصفها، وحدد موقعك والوقت. الفنيين القريبين يقبلون الطلب، وأنت تختار واحد منهم.</p>

  <h2>كيف يتحدد السعر؟</h2>
  <p>في خدمات الصيانة يجيك الفني ويكشف، وبعدها يرسل لك السعر في التطبيق. لو وافقت تدفع السعر بس. ولو ما وافقت تدفع له الكشفية (10 ريال). في التنظيف ومكافحة الحشرات ونقل العفش يرسل الفني سعره قبل ما تختاره.</p>

  <h2>كيف أدفع؟</h2>
  <p>الدفع حالياً كاش للفني بعد ما يخلص الشغل، وبعدها تأكد الدفع من التطبيق.</p>

  <h2>وش يغطي الضمان؟</h2>
  <p>كل شغل مضمون 30 يوم من تاريخ اكتمال الطلب. لو رجعت نفس المشكلة، راسلنا برقم الطلب ونرجّع لك الفني بدون مقابل.</p>

  <h2>كيف ألغي طلب؟</h2>
  <p>تقدر تلغي مجاناً قبل ما تختار فني، أو خلال 5 دقايق من اختياره.</p>

  <h2>كيف أحذف حسابي؟</h2>
  <p>من التطبيق: «حسابي» ثم «حذف الحساب». تنمسح بياناتك الشخصية مباشرة. ولو ما تقدر تدخل التطبيق، راسلنا من رقم جوالك المسجّل ونحذفه لك.</p>

  <h2>أنا فني، كيف أسجّل؟</h2>
  <p>حمّل التطبيق واختر «أنا فني»، وعبّ بياناتك وتخصصاتك. نراجع الطلب ونفعّل حسابك، وبعدها توصلك الطلبات القريبة منك.</p>
</section>
<section dir="ltr" lang="en">
  <h1>Support</h1>
  <p>Questions or a problem with a request? Email us at %(mail)s with your request number and registered mobile number.</p>
  <h2>Deleting your account</h2>
  <p>In the app: Account → Delete account. Your personal data is erased immediately. If you can't sign in, email us from your registered number and we will delete it for you.</p>
  <h2>Payment and warranty</h2>
  <p>Payment is currently in cash to the technician after the work is done. Every job carries a 30-day warranty from completion.</p>
</section>
""" % {'mail': MAIL})

# ---------------------------------------------------------------- privacy
page('privacy.html', 'سياسة الخصوصية', """
<section>
  <h1>سياسة الخصوصية</h1>
  <p class="muted">آخر تحديث: %(ar)s</p>
  <p>هذه السياسة توضّح وش البيانات اللي يجمعها تطبيق «كل شي» وكيف نستخدمها ونحميها. المسؤول عن بياناتك هو تطبيق «كل شي»، وتقدر تتواصل معنا على %(mail)s.</p>

  <h2>البيانات اللي نجمعها</h2>
  <ul>
    <li><b>بيانات الحساب:</b> رقم الجوال، الاسم، ولغة التطبيق.</li>
    <li><b>بيانات الطلب:</b> نوع الخدمة، وصف المشكلة، العنوان، والصور والفيديو والتسجيل الصوتي اللي ترفقها.</li>
    <li><b>الموقع:</b> موقعك وقت إرسال الطلب عشان نوصله لفنيين قريبين. وللفني: موقع شغله، وموقعه الحالي وهو «متاح» لاستقبال الطلبات.</li>
    <li><b>بيانات الفني:</b> رقم الهوية أو الإقامة، المدينة، التخصصات، ونطاق الشغل، والآيبان إن أضافه.</li>
    <li><b>بيانات الاستخدام:</b> حالة الطلبات، الأسعار، التقييمات، ورمز الإشعارات الخاص بجهازك.</li>
  </ul>
  <p>ما نجمع بيانات بطاقات بنكية. الدفع حالياً كاش بين العميل والفني.</p>

  <h2>كيف نستخدمها</h2>
  <ul>
    <li>توصيل طلبك للفنيين المناسبين وتنفيذه ومتابعته.</li>
    <li>إرسال كود التحقق والإشعارات عن حالة طلبك.</li>
    <li>التحقق من الفنيين، وتطبيق الضمان، وحل الشكاوى.</li>
    <li>حماية المستخدمين ومنع إساءة الاستخدام.</li>
  </ul>
  <p>ما نبيع بياناتك، وما نستخدمها للإعلانات، وما نتتبعك في تطبيقات أو مواقع ثانية.</p>

  <h2>مع مين نشاركها</h2>
  <ul>
    <li><b>الطرف الثاني في الطلب:</b> الفني اللي تختاره يشوف اسمك ورقم جوالك وعنوانك وموقع الطلب ومرفقاته. وأنت تشوف اسم الفني ورقمه وتقييمه. الفنيين القريبين يشوفون وصف الطلب ومرفقاته والعنوان قبل ما يقبلون.</li>
    <li><b>مزوّدي الخدمة:</b> Supabase (الاستضافة وقاعدة البيانات)، Authentica (رسائل التحقق)، Expo وApple وGoogle (الإشعارات). يعالجون البيانات لتشغيل الخدمة بس.</li>
    <li><b>الجهات الرسمية:</b> إذا طُلب منا ذلك نظاماً.</li>
  </ul>
  <p>رقم هوية الفني وآيبانه ما يظهر لأي مستخدم، ويطّلع عليه فريق الإدارة فقط.</p>

  <h2>وين تنحفظ البيانات</h2>
  <p>تنحفظ على خوادم Supabase خارج المملكة (منطقة مومباي، الهند)، وتنتقل مشفّرة. باستخدامك للتطبيق أنت توافق على هذا النقل.</p>

  <h2>مدة الحفظ والحذف</h2>
  <p>نحتفظ ببياناتك طول ما حسابك فعّال. تقدر تحذف حسابك من التطبيق («حسابي» ثم «حذف الحساب») أو بمراسلتنا. عند الحذف تنمسح بياناتك الشخصية (الاسم، رقم الجوال، العناوين، بيانات الفني)، وتبقى سجلات الطلبات السابقة بدون اسمك لأغراض المحاسبة وحل النزاعات.</p>

  <h2>حقوقك</h2>
  <p>لك حق تطّلع على بياناتك، وتصحّحها، وتطلب نسخة منها، وتحذفها. راسلنا على %(mail)s ونرد خلال 30 يوم.</p>

  <h2>الأذونات في جوالك</h2>
  <p>التطبيق يطلب إذن الموقع (لتحديد مكان الطلب)، والكاميرا والصور والمايكروفون (لإرفاق وصف المشكلة)، والإشعارات. تقدر توقف أي إذن من إعدادات الجوال، وبعض المزايا ما تشتغل بدونه.</p>

  <h2>الأطفال</h2>
  <p>التطبيق مو موجّه للأطفال، وما نجمع بياناتهم عن قصد. ومن هو أقل من 18 سنة يستخدمه بموافقة ولي أمره.</p>

  <h2>التغييرات</h2>
  <p>لو غيّرنا هذه السياسة ننشر النسخة الجديدة في هذه الصفحة مع تاريخ التحديث.</p>
</section>
<section dir="ltr" lang="en">
  <h1>Privacy Policy</h1>
  <p class="muted">Last updated: %(en)s</p>
  <p>This policy explains what the Kul Shay app collects and how it is used. The data controller is the Kul Shay app; contact us at %(mail)s.</p>
  <h2>What we collect</h2>
  <ul>
    <li><b>Account:</b> mobile number, name and app language.</li>
    <li><b>Requests:</b> service type, description, address, and the photos, video and voice note you attach.</li>
    <li><b>Location:</b> your location when you send a request, so it reaches nearby technicians. For technicians: work location, and current location while set to "available".</li>
    <li><b>Technicians:</b> national ID or Iqama number, city, trades, service radius, and IBAN if provided.</li>
    <li><b>Usage:</b> request status, prices, ratings, and your device's push-notification token.</li>
  </ul>
  <p>We do not collect card details. Payment is currently in cash between customer and technician.</p>
  <h2>How we use it</h2>
  <p>To match and carry out your request, send verification codes and status notifications, verify technicians, honour the warranty, resolve complaints, and prevent abuse. We do not sell your data, use it for advertising, or track you across other apps or websites.</p>
  <h2>Who we share it with</h2>
  <ul>
    <li><b>The other party to a request:</b> the technician you choose sees your name, mobile number, address, request location and attachments; you see the technician's name, number and rating. Nearby technicians see the description, attachments and address before accepting.</li>
    <li><b>Service providers:</b> Supabase (hosting and database), Authentica (verification SMS), Expo, Apple and Google (push notifications), solely to run the service.</li>
    <li><b>Authorities:</b> when legally required.</li>
  </ul>
  <p>A technician's ID number and IBAN are never shown to other users.</p>
  <h2>Where it is stored</h2>
  <p>On Supabase servers outside Saudi Arabia (Mumbai, India), encrypted in transit. By using the app you consent to this transfer.</p>
  <h2>Retention and deletion</h2>
  <p>We keep your data while your account is active. You can delete your account in the app (Account → Delete account) or by emailing us. Deletion erases your personal data (name, mobile number, addresses, technician details); past request records are kept without your name for accounting and dispute resolution.</p>
  <h2>Your rights</h2>
  <p>You may access, correct, obtain a copy of, or delete your data. Email %(mail)s and we will respond within 30 days.</p>
  <h2>Children</h2>
  <p>The app is not directed at children and we do not knowingly collect their data. Anyone under 18 should use it with a parent or guardian's consent.</p>
  <h2>Changes</h2>
  <p>Updates to this policy are published on this page with a new date.</p>
</section>
""" % {'ar': UPDATED_AR, 'en': UPDATED_EN, 'mail': MAIL})

# ---------------------------------------------------------------- terms
page('terms.html', 'الشروط والأحكام', """
<section>
  <h1>الشروط والأحكام</h1>
  <p class="muted">آخر تحديث: %(ar)s</p>
  <p>باستخدامك لتطبيق «كل شي» أنت توافق على هذه الشروط. إذا ما توافق عليها لا تستخدم التطبيق.</p>

  <h2>وش هو «كل شي»</h2>
  <p>«كل شي» منصة تجمع العملاء بفنيين صيانة مستقلين. الفني يقدّم الخدمة باسمه وعلى مسؤوليته، والتطبيق وسيط ينظّم الطلب ويتابعه، وما هو طرف في عقد الخدمة بين العميل والفني.</p>

  <h2>الحساب</h2>
  <ul>
    <li>تسجّل برقم جوالك الصحيح. ومن هو أقل من 18 سنة يستخدم التطبيق بموافقة ولي أمره.</li>
    <li>أنت مسؤول عن كل استخدام يصير من حسابك.</li>
    <li>الفني لازم يدخل بيانات صحيحة، ويتفعّل حسابه بعد مراجعة الإدارة.</li>
  </ul>

  <h2>الطلبات والأسعار</h2>
  <ul>
    <li><b>خدمات الصيانة:</b> الفني يكشف في الموقع ثم يرسل السعر في التطبيق (أجرة الشغل والقطع). إذا وافقت تدفع السعر فقط. إذا رفضت تدفع للفني الكشفية المعلنة في التطبيق (حالياً 10 ريال).</li>
    <li><b>التنظيف ومكافحة الحشرات ونقل العفش:</b> الفني يرسل سعره وهو يقبل الطلب، وأنت تختار.</li>
    <li>السعر المتفق عليه في التطبيق هو المعتمد. أي اتفاق خارج التطبيق ما يشمله الضمان.</li>
  </ul>

  <h2>الدفع</h2>
  <p>الدفع حالياً كاش من العميل للفني بعد اكتمال الشغل، ويأكده أحد الطرفين في التطبيق. قد نضيف الدفع الإلكتروني لاحقاً.</p>

  <h2>الإلغاء</h2>
  <p>للعميل الإلغاء مجاناً قبل اختيار فني، أو خلال 5 دقايق من اختياره. بعد وصول الفني والكشف تُطبّق الكشفية إذا ما تم الاتفاق على السعر.</p>

  <h2>الضمان</h2>
  <p>كل شغل مكتمل عن طريق التطبيق مضمون 30 يوم من تاريخ الاكتمال. إذا رجعت نفس المشكلة يرجع الفني لإصلاحها بدون أجرة. الضمان ما يشمل الأعطال الجديدة، ولا سوء الاستخدام، ولا القطع اللي وفّرها العميل.</p>

  <h2>للفنيين</h2>
  <ul>
    <li>اشتراك سنوي (حالياً 50 ريال) لاستقبال الطلبات.</li>
    <li>عمولة للمنصة (حالياً 10%%) من أجرة الشغل فقط، وما تنحسب على القطع. تظهر في المحفظة وتُسدّد للمنصة.</li>
    <li>الالتزام بالموعد، والسعر المرسل في التطبيق، وصور قبل وبعد، وجودة الشغل.</li>
  </ul>

  <h2>الاستخدام المقبول</h2>
  <p>يُمنع إدخال بيانات غير صحيحة، أو طلبات وهمية، أو الإساءة للطرف الثاني، أو التحايل على عمولة المنصة، أو استخدام التطبيق في أي شي مخالف للنظام. لنا حق إيقاف أي حساب يخالف هذه الشروط.</p>

  <h2>المسؤولية</h2>
  <p>نحرص على توثيق الفنيين ومتابعة الجودة، لكن الفني هو المسؤول عن شغله وعن أي ضرر ينتج عنه. مسؤولية التطبيق في كل الأحوال ما تتجاوز قيمة الطلب محل الخلاف، في الحدود اللي يسمح بها النظام.</p>

  <h2>النظام المطبّق</h2>
  <p>تخضع هذه الشروط لأنظمة المملكة العربية السعودية، وتختص محاكمها بأي نزاع.</p>

  <h2>التواصل</h2>
  <p>لأي استفسار: %(mail)s</p>
</section>
<section dir="ltr" lang="en">
  <h1>Terms of Use</h1>
  <p class="muted">Last updated: %(en)s</p>
  <p>By using the Kul Shay app you agree to these terms.</p>
  <h2>What Kul Shay is</h2>
  <p>A marketplace connecting customers with independent maintenance technicians. Technicians provide services in their own name and at their own responsibility; the app is an intermediary and is not a party to the service contract.</p>
  <h2>Accounts</h2>
  <p>Register with your own mobile number. Anyone under 18 should use the app with a parent or guardian's consent. You are responsible for activity on your account. Technician accounts are activated after review.</p>
  <h2>Requests and prices</h2>
  <p>For maintenance services the technician inspects on site and sends a price in the app (labor and parts). If you approve, you pay only that price; if you decline, you pay the inspection fee shown in the app (currently SAR 10). For cleaning, pest control and moving, technicians send their price when accepting. The price agreed in the app is the binding one.</p>
  <h2>Payment</h2>
  <p>Payment is currently in cash from the customer to the technician after the work, confirmed in the app by either party.</p>
  <h2>Cancellation</h2>
  <p>Free before choosing a technician, or within 5 minutes of choosing one.</p>
  <h2>Warranty</h2>
  <p>Completed jobs carry a 30-day warranty: if the same problem returns, the technician comes back at no labor charge. New faults, misuse and customer-supplied parts are excluded.</p>
  <h2>Technicians</h2>
  <p>A yearly subscription (currently SAR 50) and a platform commission (currently 10%%) on labor only, not parts.</p>
  <h2>Acceptable use and liability</h2>
  <p>No false information, fake requests, abuse, or circumventing the platform. We may suspend accounts that break these terms. Technicians are responsible for their work; the app's liability is limited to the value of the request in dispute, to the extent the law allows.</p>
  <h2>Governing law</h2>
  <p>The laws of the Kingdom of Saudi Arabia. Contact: %(mail)s</p>
</section>
""" % {'ar': UPDATED_AR, 'en': UPDATED_EN, 'mail': MAIL})

print('built', sorted(os.listdir('docs')))
