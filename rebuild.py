import os, base64
from PIL import Image
import io

base = r'C:\Users\liwen\Dropbox\PC (2)\Desktop\l289\EDM技能\波西傑克森'

# prepare base64
hero_files = [f for f in os.listdir(os.path.join(base, 'generated')) if f.startswith('hero-percy-jackson') and f.endswith('.jpg') and '1300' in f]
with open(os.path.join(base, 'generated', hero_files[0]), 'rb') as f:
    hero_b64 = base64.b64encode(f.read()).decode()

img = Image.open(os.path.join(base, 'page1_img1.png'))
ratio = 600 / img.width
img = img.resize((600, int(img.height * ratio)), Image.LANCZOS)
buf = io.BytesIO()
img.save(buf, 'JPEG', quality=75)
page_b64 = base64.b64encode(buf.getvalue()).decode()

hero_uri = 'data:image/jpeg;base64,' + hero_b64
page_uri = 'data:image/jpeg;base64,' + page_b64

print(f'hero_uri len: {len(hero_uri)}')
print(f'page_uri len: {len(page_uri)}')

# ========== email-template.html ==========
email_template = """<html>
<body bgcolor="#F3EFE8">

<!-- TOP DECO BAR -->
<table width="620" cellpadding="0" cellspacing="0" border="0" align="center">
  <tbody>
    <tr>
      <td width="207" height="5" bgcolor="#C4815A"></td>
      <td width="206" height="5" bgcolor="#7D9B6A"></td>
      <td width="207" height="5" bgcolor="#6B8FA3"></td>
    </tr>
  </tbody>
</table>

<!-- MAIN CONTENT -->
<table width="620" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFF9F2" align="center">
  <tbody>

    <!-- HERO -->
    <tr>
      <td align="center">
        <img src="HERO_URI" width="620" border="0" alt="卿鬆翻一頁" title="卿鬆翻一頁" style="display:block; margin:0 auto; text-align:center;">
      </td>
    </tr>

    <tr><td height="28"></td></tr>

    <!-- 主標題 -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564" align="left">
                <font face="Arial, sans-serif" size="5" color="#4A6B3E"><b>翻一頁，開始你的希臘神話冒險</b></font><br>
                <font face="Arial, sans-serif" size="2" color="#7A6B5A">波西傑克森1：神火之賊</font>
                <hr size="1" width="100%" color="#D9CFC4">
                <font face="Arial, sans-serif" size="4" color="#3D2C1A">
                  嗨嗨！我是卿鬆。不知道你是不是也跟我一樣，有一天發現這個世界再也無法讓你逃離吵雜的生活。跟著我，找回生活的專注與平靜。在這個專屬空間裡，除了有精心挑選的書中精華，文末也為你準備了暖心的小驚喜！
                </font>
                <br><br>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr><td height="12"></td></tr>

    <!-- 內文段落 -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564" align="left">
                <font face="Arial, sans-serif" size="4" color="#3D2C1A">
                  不知道有沒有人跟我一樣雖然老大不小，但還是依舊很喜歡看青少年的小說。總是會幻想在我們看不到的地方是不是真的有這些世界，而且每天都是神仙妖魔在打架，只是我們是麻瓜所以都不知道。
                </font>
                <br><br>
                <font face="Arial, sans-serif" size="4" color="#3D2C1A">
                  這一集男主角波西真的好倒楣，因為爸爸是海神波塞頓被針對，還莫名被栽贓是小偷偷走宙斯的「閃電火」，差點引起兄弟鬩牆、世界大戰，只能想辦法自證清白。
                </font>
                <br><br>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr><td height="12"></td></tr>

    <!-- 書摘圖片 -->
    <tr>
      <td align="center">
        <img src="PAGE_URI" width="564" border="0" alt="波西傑克森書摘圖片" style="display:block; margin:0 auto; text-align:center;">
      </td>
    </tr>

    <tr><td height="22"></td></tr>

    <!-- SECTION: 希臘神話亮點 -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564" align="left">
                <font face="Arial, sans-serif" size="2" color="#7D9B6A"><b>- 希 臘 神 話 亮 點 -</b></font>
                <br><br>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <!-- 亮點列表 -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564">
                <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F6F2EC">
                  <tbody>
                    <tr>
                      <td width="4" bgcolor="#6B8F5E"></td>
                      <td width="16"></td>
                      <td align="left">
                        <br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          <b>眾神八卦</b><br>
                          希臘神話最有趣的莫過於那些眾神之間的愛恨情仇，每個神都超有個性
                        </font>
                        <br><br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          <b>帝國大廈600樓</b><br>
                          宙斯就住在帝國大廈600樓！這種與現實重疊的描述讓一切都不再遙不可及
                        </font>
                        <br><br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          <b>經典反派</b><br>
                          對到眼就石化的梅杜莎，經典不敗的反派角色
                        </font>
                        <br><br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          <b>青少年冒險</b><br>
                          主角就是位十幾歲的青少年，看這本書的時候好像忘記長大的煩惱
                        </font>
                        <br><br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          <b>暫時喘口氣</b><br>
                          如果被現實生活壓得喘不過氣，這本小說很適合讓你暫時逃離
                        </font>
                        <br><br>
                      </td>
                      <td width="16"></td>
                    </tr>
                  </tbody>
                </table>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr><td height="22"></td></tr>

    <!-- CTA -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564">
                <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#6B8F5E">
                  <tbody>
                    <tr>
                      <td width="8" bgcolor="#4A6B3E"></td>
                      <td width="20"></td>
                      <td align="center">
                        <br>
                        <font face="Arial, sans-serif" size="4" color="#FFFFFF"><b>一起翻開波西傑克森</b></font>
                        <br><br>
                        <font face="Arial, sans-serif" size="4" color="#FFFFFF">跟著主角一起盡情的衝動冒險闖世界</font>
                        <br><br>
                      </td>
                      <td width="20"></td>
                      <td width="8" bgcolor="#4A6B3E"></td>
                    </tr>
                  </tbody>
                </table>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr><td height="18"></td></tr>

    <!-- READER GIFT -->
    <tr>
      <td>
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td width="28"></td>
              <td width="564">
                <table width="100%" cellpadding="0" cellspacing="0" border="2" bordercolor="#D8B49B" bgcolor="#FFF6EF">
                  <tbody>
                    <tr>
                      <td align="center">
                        <br>
                        <font face="Arial, sans-serif" size="4" color="#4A3525">
                          感謝您今天的閱報，讀者禮「<b><font color="#9E6340">10元購物金</font></b>」限量100份<br>
                          輸入兌換碼「<b><font color="#9E6340">卿鬆去冒險</font></b>」就可以兌換（發報七日內有效）<br>
                          卿鬆翻一頁，我們下頁見！
                        </font>
                        <br><br>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
              <td width="28"></td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>

    <tr><td height="18"></td></tr>

    <!-- UNSUBSCRIBE -->
    <tr>
      <td align="center">
        <font face="Arial, sans-serif" size="2" color="#8B7D72">
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSfBeuECJmAnhRDTRv-i6509RGbg3VRolu7_BuAPBPM9pnNXCQ/viewform" target="_blank" rel="noreferrer noopener">
            <font color="#8B7D72">不想收到卿鬆小編的信請點我</font>
          </a>
        </font>
      </td>
    </tr>

    <tr><td height="18"></td></tr>

    <!-- FOOTER -->
    <tr>
      <td align="center">
        <font face="Arial, sans-serif" size="2" color="#7A6B5A">卿鬆翻一頁 (c) 2026</font>
      </td>
    </tr>

    <tr><td height="24"></td></tr>

  </tbody>
</table>

<!-- BOTTOM DECO BAR -->
<table width="620" cellpadding="0" cellspacing="0" border="0" align="center">
  <tbody>
    <tr>
      <td width="207" height="5" bgcolor="#C4815A"></td>
      <td width="206" height="5" bgcolor="#7D9B6A"></td>
      <td width="207" height="5" bgcolor="#6B8FA3"></td>
    </tr>
  </tbody>
</table>

</body>
</html>"""

email_html = email_template.replace('HERO_URI', hero_uri).replace('PAGE_URI', page_uri)

with open(os.path.join(base, 'email-template.html'), 'w', encoding='utf-8') as f:
    f.write(email_html)
print(f'email-template.html: {len(email_html)} bytes')

# ========== blog-template.html ==========
blog_template = """<div style="max-width:680px; margin:0 auto; padding:28px 16px 48px; box-sizing:border-box; font-family:'Noto Sans TC','PingFang TC','Microsoft JhengHei',Arial,sans-serif; line-height:1.8; color:#3D2C1A; background:#F3EFE8;">

  <!-- Hero -->
  <div style="width:100%; border-radius:14px; overflow:hidden; box-shadow:0 4px 20px rgba(0,0,0,0.10); margin-bottom:24px;">
    <img src="HERO_URI" alt="卿鬆翻一頁" style="display:block; width:100%; max-width:100%; height:auto; border:0; margin:0 auto;">
  </div>

  <!-- Intro card -->
  <div style="background:#FFFCF8; border-radius:14px; box-shadow:0 2px 12px rgba(0,0,0,0.06); padding:32px 28px; margin-bottom:20px;">
    <h1 style="margin:0 0 4px; font-size:25px; font-weight:700; color:#4A6B3E; letter-spacing:0.03em; line-height:1.3;">翻一頁，開始你的希臘神話冒險</h1>
    <div style="font-size:14px; color:#7A6B5A; margin-bottom:20px; padding-bottom:16px; border-bottom:2px solid #EDE8E0;">波西傑克森1：神火之賊</div>
    <p style="font-size:15px; line-height:1.8; color:#3D2C1A; margin:0 0 12px;">
      嗨嗨！我是卿鬆。不知道你是不是也跟我一樣，有一天發現這個世界再也無法讓你逃離吵雜的生活。跟著我，找回生活的專注與平靜。在這個專屬空間裡，除了有精心挑選的書中精華，文末也為你準備了暖心的小驚喜！
    </p>
    <p style="font-size:15px; line-height:1.8; color:#3D2C1A; margin:0 0 12px;">
      不知道有沒有人跟我一樣雖然老大不小，但還是依舊很喜歡看青少年的小說。總是會幻想在我們看不到的地方是不是真的有這些世界，而且每天都是神仙妖魔在打架，只是我們是麻瓜所以都不知道。
    </p>
    <p style="font-size:15px; line-height:1.8; color:#3D2C1A; margin:0;">
      這一集男主角波西真的好倒楣，因為爸爸是海神波塞頓被針對，還莫名被栽贓是小偷偷走宙斯的「閃電火」，差點引起兄弟鬩牆、世界大戰，只能想辦法自證清白。
    </p>
  </div>

  <!-- 書摘圖片 -->
  <div style="text-align:center; margin-bottom:20px;">
    <img src="PAGE_URI" alt="波西傑克森書摘圖片" style="display:block; max-width:100%; height:auto; border-radius:10px; box-shadow:0 2px 12px rgba(0,0,0,0.08); margin:0 auto;">
  </div>

  <!-- Features -->
  <div style="background:#FFFCF8; border-radius:14px; box-shadow:0 2px 12px rgba(0,0,0,0.06); padding:28px 28px 8px; margin-bottom:20px;">
    <div style="text-align:center; margin:0 0 18px; font-size:13px; letter-spacing:0.25em; color:#6B8F5E;">
      <span style="display:inline-block; width:30px; height:1px; background:#6B8F5E; opacity:0.3; vertical-align:middle; margin-right:8px;"></span>
      希 臘 神 話 亮 點
      <span style="display:inline-block; width:30px; height:1px; background:#6B8F5E; opacity:0.3; vertical-align:middle; margin-left:8px;"></span>
    </div>

    <div style="display:flex; gap:14px; padding:14px 0; border-bottom:1px solid #EDE8E0; align-items:flex-start;">
      <span style="font-size:22px; flex-shrink:0; width:36px; text-align:center;">&#9889;</span>
      <span style="font-size:15px; line-height:1.7;"><b>眾神八卦</b> - 希臘神話最有趣的莫過於那些眾神之間的愛恨情仇，每個神都超有個性</span>
    </div>

    <div style="display:flex; gap:14px; padding:14px 0; border-bottom:1px solid #EDE8E0; align-items:flex-start;">
      <span style="font-size:22px; flex-shrink:0; width:36px; text-align:center;">&#127963;</span>
      <span style="font-size:15px; line-height:1.7;"><b>帝國大廈600樓</b> - 宙斯就住在帝國大廈600樓！這種與現實重疊的描述讓一切都不再遙不可及</span>
    </div>

    <div style="display:flex; gap:14px; padding:14px 0; border-bottom:1px solid #EDE8E0; align-items:flex-start;">
      <span style="font-size:22px; flex-shrink:0; width:36px; text-align:center;">&#128013;</span>
      <span style="font-size:15px; line-height:1.7;"><b>經典反派</b> - 對到眼就石化的梅杜莎，經典不敗的反派角色</span>
    </div>

    <div style="display:flex; gap:14px; padding:14px 0; border-bottom:1px solid #EDE8E0; align-items:flex-start;">
      <span style="font-size:22px; flex-shrink:0; width:36px; text-align:center;">&#128313;</span>
      <span style="font-size:15px; line-height:1.7;"><b>青少年冒險</b> - 主角就是位十幾歲的青少年，看這本書的時候好像忘記長大的煩惱</span>
    </div>

    <div style="display:flex; gap:14px; padding:14px 0; align-items:flex-start;">
      <span style="font-size:22px; flex-shrink:0; width:36px; text-align:center;">&#127754;</span>
      <span style="font-size:15px; line-height:1.7;"><b>暫時喘口氣</b> - 如果被現實生活壓得喘不過氣，這本小說很適合讓你暫時逃離</span>
    </div>
  </div>

  <!-- CTA -->
  <div style="background:linear-gradient(135deg, #6B8F5E, #4A6B3E); border-radius:14px; padding:30px 24px; text-align:center; color:#fff; margin-bottom:20px;">
    <h2 style="margin:0 0 6px; font-size:20px; font-weight:700;">一起翻開波西傑克森</h2>
    <p style="margin:0; font-size:14.5px; opacity:0.92;">跟著主角一起盡情的衝動冒險闖世界</p>
  </div>

  <!-- Reader Gift -->
  <div style="text-align:center; border:2px dashed #6B8F5E; background:#FFFCF8; border-radius:14px; padding:22px 24px; margin-bottom:20px;">
    <p style="margin:0; font-size:15px; line-height:1.8; color:#4A3525;">
      感謝您的今天的閱報，讀者禮「<strong style="color:#4A6B3E;">10元購物金</strong>」限量100份<br>
      輸入兌換碼「<strong style="color:#4A6B3E;">卿鬆去冒險</strong>」就可以兌換（發報七日內有效）<br>
      卿鬆翻一頁，我們下頁見！
    </p>
  </div>

  <!-- Footer -->
  <div style="text-align:center; padding-top:16px; border-top:1px solid #E0D8CC; font-size:13px; color:#7A6B5A;">
    <p style="margin:0;">卿鬆翻一頁 (c) 2026</p>
  </div>

</div>"""

blog_html = blog_template.replace('HERO_URI', hero_uri).replace('PAGE_URI', page_uri)

with open(os.path.join(base, 'blog-template.html'), 'w', encoding='utf-8') as f:
    f.write(blog_html)
print(f'blog-template.html: {len(blog_html)} bytes')

print('done')
