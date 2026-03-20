import re

file_path = r'g:\我的雲端硬碟\2025_lee\+++++專案\++++++核點創意Nudot\web_site\nd\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Google fonts
if 'fonts.googleapis.com' not in content:
    content = content.replace('<title>NUDOT. CREATIVE</title>', '<title>NUDOT. CREATIVE</title>\n  <!-- 引入 Google Fonts -->\n  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Playfair+Display:ital,wght@1,400;1,700&display=swap" rel="stylesheet">')

# 2. Add new CSS variables to :root
root_new = '''    :root {
      --bg-color: #000000;
      --text-color: #ffffff;
      --subtext-color: #888888;
      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
      --text-white: #ffffff;
      --accent-white: rgba(255, 255, 255, 0.85);
    }'''
content = re.sub(r' *:root *\{[^}]*\}', root_new, content)

# 3. Replace old CSS with new CSS
# Old css starts at /* 主視覺區塊 */ and ends before /* --- 新增：第二區塊 (Works) 樣式 --- */
new_css = '''    /* 背景容器 */
    .hero-container {
        position: relative;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* YouTube 背景影片樣式：確保填滿螢幕並隱藏互動 */
    .video-background {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 100vw;
        height: 56.25vw; /* 16:9 比例 */
        min-height: 100vh;
        min-width: 177.77vh; /* 比例反推 */
        transform: translate(-50%, -50%);
        z-index: -2;
        pointer-events: none; /* 防止使用者點擊到 YouTube 介面 */
        background: #000;
        border: none;
    }

    /* 影片上的遮罩 */
    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.4); /* 稍微加深遮罩，配合 YT 影片亮度 */
        z-index: -1;
    }

    /* 頂部裝飾欄 */
    .top-notch {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 120px;
        height: 50px;
        background: #ffffff;
        border-radius: 0 0 60px 60px;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10;
    }

    .top-notch::after {
        content: '↓';
        color: #000;
        font-size: 1.2rem;
    }

    /* 左上角內容 */
    .top-left-content {
        position: absolute;
        top: 40px;
        left: 40px;
        width: 250px;
        opacity: 0;
    }

    .studio-desc {
        font-size: 11px;
        line-height: 1.4;
        color: var(--text-white);
        margin-bottom: 20px;
        text-transform: lowercase;
        letter-spacing: 0.5px;
    }

    .nav-arrows {
        display: flex;
        gap: 10px;
        align-items: center;
        color: var(--text-white);
    }

    .arrow {
        font-size: 14px;
        cursor: pointer;
    }

    /* 右上角內容 */
    .top-right-content {
        position: absolute;
        top: 40px;
        right: 40px;
        text-align: right;
        opacity: 0;
        color: var(--text-white);
    }

    .top-right-content p {
        font-size: 14px;
        margin-bottom: 5px;
        text-transform: lowercase;
        letter-spacing: 1px;
    }

    .ux-ui-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: white;
        border-radius: 50%;
        margin-left: 10px;
    }

    /* 中央探索按鈕 */
    .explore-btn {
        position: absolute;
        top: 40%;
        left: 45%;
        transform: translate(-50%, -50%);
        width: 100px;
        height: 100px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        z-index: 5;
        transition: all 0.3s ease;
        opacity: 0;
        color: var(--text-white);
    }

    .explore-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translate(-50%, -50%) scale(1.1);
    }

    .explore-text {
        font-size: 10px;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }

    /* 主要標題排版 */
    .main-title-wrap {
        position: absolute;
        bottom: 10%;
        width: 90%;
        display: flex;
        flex-direction: column;
        pointer-events: none;
    }

    .title-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: -20px;
    }

    .title-text {
        font-size: clamp(60px, 12vw, 150px);
        font-weight: 700;
        text-transform: uppercase;
        line-height: 0.9;
        letter-spacing: -2px;
        color: var(--text-white);
    }

    .title-subtext {
        font-size: 16px;
        width: 200px;
        text-align: right;
        margin-bottom: 40px;
        line-height: 1.2;
        text-transform: lowercase;
        color: var(--text-white);
    }

    .studio-text {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-weight: 400;
        margin-left: 20px;
        color: var(--text-white);
    }

    /* 底部裝飾 */
    .bottom-left-info {
        position: absolute;
        bottom: 40px;
        left: 40px;
        opacity: 0;
    }

    .our-projects {
        font-size: 18px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        color: var(--text-white);
    }

    .arrow-circle {
        width: 24px;
        height: 24px;
        border: 1px solid white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 12px;
    }

    .pagination {
        position: absolute;
        bottom: 40px;
        right: 40px;
        display: flex;
        gap: 8px;
        opacity: 0;
    }

    .dot {
        width: 8px;
        height: 8px;
        border: 1px solid white;
        border-radius: 50%;
    }

    .dot.active {
        background: white;
    }

    /* 裝飾性星星與圖標 */
    .star-icon {
        position: absolute;
        pointer-events: none;
        opacity: 0;
    }

    .sparkle {
        position: absolute;
        top: 50%;
        left: 20%;
        width: 40px;
        height: 40px;
    }

    .small-icons {
        position: absolute;
        left: 200px;
        bottom: 42%;
        display: flex;
        gap: 15px;
        opacity: 0;
    }

    .icon-circle {
        width: 35px;
        height: 35px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 8px;
        color: var(--text-white);
    }
'''
content = re.sub(r'/\* 主視覺區塊 \*/.*?/\* --- 新增：第二區塊 \(Works\) 樣式 --- \*/', new_css + '\n    /* --- 新增：第二區塊 (Works) 樣式 --- */', content, flags=re.DOTALL)

# 4. Remove old media query mobile adjustments for main/hero
content = re.sub(r' +/\* 主標題 \*/.*?(?= +/\* Works section \*/)', '', content, flags=re.DOTALL)
content = re.sub(r' +/\* --- Hero --- \*/.*?(?= +/\* --- Works section --- \*/)', '', content, flags=re.DOTALL)
content = re.sub(r' +\.hero-title \{.*?\.works-heading', '      .works-heading', content, flags=re.DOTALL)

# 5. Replace <main> block
new_main = '''  <main class="hero-container">
        <!-- YouTube 背景影片：加入參數使其自動播放、靜音、循環、隱藏控制項 -->
        <iframe class="video-background" 
                src="https://www.youtube.com/embed/tdZUcouI8nU?autoplay=1&mute=1&loop=1&playlist=tdZUcouI8nU&controls=0&showinfo=0&rel=0&iv_load_policy=3&modestbranding=1" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                referrerpolicy="strict-origin-when-cross-origin"></iframe>
        
        <!-- 背景遮罩 -->
        <div class="overlay"></div>

        <!-- 頂部 U 型槽 -->
        <div class="top-notch"></div>

        <!-- 左上文字與箭頭 -->
        <div class="top-left-content">
            <p class="studio-desc">our studio is dedicated to crafting visually stunning and engaging digital experiences</p>
            <div class="nav-arrows">
                <span class="arrow">← —— →</span>
            </div>
        </div>

        <!-- 右上分類 -->
        <div class="top-right-content">
            <p>creative design</p>
            <p>branding</p>
            <p>ux/ui <span class="ux-ui-dot"></span></p>
        </div>

        <!-- 中央探索圓圈 -->
        <div class="explore-btn" id="exploreBtn">
            <span class="explore-text">explore</span>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
        </div>

        <!-- 中間左側小圖標 -->
        <div class="small-icons">
            <div class="icon-circle">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
            </div>
            <div class="icon-circle">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            </div>
        </div>

        <!-- 十字星裝飾 -->
        <svg class="star-icon sparkle" viewBox="0 0 100 100" fill="white">
            <path d="M50 0 L52 48 L100 50 L52 52 L50 100 L48 52 L0 50 L48 48 Z" />
        </svg>

        <!-- 主要大標題 -->
        <div class="main-title-wrap">
            <div class="title-row">
                <h1 class="title-text" id="title1">Creative</h1>
                <p class="title-subtext">conquer the highest peaks with us</p>
                <h1 class="title-text" id="title2">Design</h1>
            </div>
            <div class="title-row">
                <h1 class="title-text" id="title3">Digital <span class="studio-text">studio</span></h1>
            </div>
        </div>

        <!-- 底部專案連結 -->
        <div class="bottom-left-info">
            <div class="our-projects">
                <span>OUR PROJECTS</span>
                <div class="arrow-circle">↓</div>
            </div>
        </div>

        <!-- 頁碼點 -->
        <div class="pagination">
            <div class="dot active"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </main>'''
content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

# 6. Replace GSAP code
new_gsap = '''      // 1. 頂部導覽列淡出(因為沒在使用，或保留作後續使用)
      tl.from(".title-text", {
          y: 100,
          opacity: 0,
          stagger: 0.2,
          skewY: 7,
          ease: "power4.out", duration: 1.5
      })
      .to(".top-left-content, .top-right-content", {
          opacity: 1,
          y: 0,
          ease: "power4.out", duration: 1.5
      }, "-=1")
      .to(".explore-btn", {
          opacity: 1,
          scale: 1,
          rotation: 360,
          duration: 2,
          ease: "power4.out"
      }, "-=1.5")
      .to(".bottom-left-info, .pagination, .small-icons", {
          opacity: 1,
          y: 0,
          ease: "power4.out", duration: 1.5
      }, "-=1")
      .to(".star-icon", {
          opacity: 0.8,
          scale: 1,
          stagger: 0.3,
          ease: "power4.out", duration: 1.5
      }, "-=1")
      .from(".title-subtext", {
          x: 50,
          opacity: 0,
          ease: "power4.out", duration: 1.5
      }, "-=1.2");'''

content = re.sub(r'      // 1\. 頂部導覽列淡入.*?ease: "power2\.out"\n *\}, "-=1\.2"\);', new_gsap, content, flags=re.DOTALL)

# 7. Remove Parallax Effect part of hero that is no longer valid
content = re.sub(r'      // 滑鼠移動視差效果 \(Parallax Effect\).*?// --- 修改：滾動 Zoom Out 無痕銜接動畫 ---', '      // --- 修改：滾動 Zoom Out 無痕銜接動畫 ---', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
