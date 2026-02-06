// Wrap every letter in a span（加个判空，避免某些页面没有 .ml3 报错）
var textWrapper = document.querySelector('.ml3');
if (textWrapper) {
  textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

  anime.timeline({loop: true})
    .add({
      targets: '.ml3 .letter',
      opacity: [0,1],
      easing: "easeInOutQuad",
      duration: 2250,
      delay: (el, i) => 150 * (i+1)
    }).add({
      targets: '.ml3',
      opacity: 0,
      duration: 1000,
      easing: "easeOutExpo",
      delay: 1000
    });
}


//全屏视频
// var video = document.getElementById("video1");
// var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

// if (isMobile) {
//   video.style.display = "none";
//   video.muted = true;
// } else {
//   video.volume = 0.5; // 或者根据需要设置适当的音量值，例如 0.5 表示 50% 的音量
// }

// 优化
// const container = document.querySelector('.container');
// const boxes = document.querySelectorAll('p');

// // Read a layout property
// const newWidth = container.offsetWidth;

// for (var i = 0; i < boxes.length; i++) {    
//     // Then invalidate layouts with writes.
//     boxes[i].style.width = newWidth + 'px';
// }
// const width = box.offsetWidth;
// box.classList.add('big');

// // When the user clicks on a link/button:
// async function navigateToSettingsPage() {
//   // Capture and visually freeze the current state.
//   await document.documentTransition.prepare({
//     rootTransition: 'cover-up',
//     sharedElements: [element1, element2, element3],
//   });
//   // This is a function within the web app:
//   updateDOMForSettingsPage();
//   // Start the transition.
//   await document.documentTransition.start({
//     sharedElements: [element1, element4, element5],
//   });
//   // Transition complete!
// }
// 优化end

// ============================================
// 没有目录时，只隐藏顶部 TOC 小按钮（保留右侧区域）
// ============================================
function updateTocToggleVisibility() {
  // 顶部用于展开 TOC 的小按钮（你截图里的 label.md-top__button[for="__toc"]）
  var tocToggleTopButton = document.querySelector('.md-top__button[for="__toc"]');
  if (!tocToggleTopButton) return;

  // 更稳的判断方式：看右侧 TOC 是否存在任何指向页面锚点（#...）的链接
  // Material 的右侧 TOC 通常在 `.md-sidebar--secondary .md-nav--secondary`
  var tocAnchorLinks = document.querySelectorAll(
    '.md-sidebar--secondary .md-nav--secondary a[href^="#"]'
  );

  // 若没找到，再兜底：右侧 sidebar 内任何 # 锚点链接都算 TOC
  if (!tocAnchorLinks || tocAnchorLinks.length === 0) {
    tocAnchorLinks = document.querySelectorAll(
      '.md-sidebar--secondary a[href^="#"]'
    );
  }

  var hasToc = !!(tocAnchorLinks && tocAnchorLinks.length > 0);

  // 显式切换，避免上一页隐藏状态“残留”
  tocToggleTopButton.style.display = hasToc ? "" : "none";
}

// 初次加载
document.addEventListener("DOMContentLoaded", updateTocToggleVisibility);

// 若开启了 instant navigation（或主题内部做了局部刷新），页面切换后也更新一次
if (window.document$ && typeof window.document$.subscribe === "function") {
  window.document$.subscribe(function () {
    updateTocToggleVisibility();
  });
}

