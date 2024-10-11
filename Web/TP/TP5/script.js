function getBrowserName(userAgent) {
  // The order matters here, and this may report false positives for unlisted browsers.

  if (userAgent.includes("Firefox")) {
    return "Mozilla Firefox";
  } else if (userAgent.includes("SamsungBrowser")) {
    return "Samsung Internet";
  } else if (userAgent.includes("Opera") || userAgent.includes("OPR")) {
    return "Opera";
  } else if (userAgent.includes("Edge")) {
    return "Microsoft Edge (Legacy)";
  } else if (userAgent.includes("Edg")) {
    return "Microsoft Edge (Chromium)";
  } else if (userAgent.includes("Chrome")) {
    return "Google Chrome or Chromium";
  } else if (userAgent.includes("Safari")) {
    return "Apple Safari";
  } else {
    return "unknown";
  }
}

function getOs(userAgent) {
  if (userAgent.includes("Win")) {
    return "Windows";
  } else if (userAgent.includes("Mac")) {
    return "Mac";
  } else if (userAgent.includes("Linux")) {
    return "Linux";
  } else if (userAgent.includes("Android")) {
    return "Android";
  } else if (userAgent.includes("iPhone")) {
    return "IOS";
  }
}

function getBrowserVersion(userAgent) {
  if (userAgent.includes("Chrome")) {
    return userAgent.match(/Chrome\/([0-9.]*)/)[1];
  } else if (userAgent.includes("Firefox")) {
    return userAgent.match(/Firefox\/([0-9.]*)/)[1];
  } else if (userAgent.includes("Edge")) {
    return userAgent.match(/Edge\/([0-9.]*)/)[1];
  }
}

const browserName = getBrowserName(navigator.userAgent);
const OsName = getOs(navigator.userAgent);
const version = getBrowserVersion(navigator.userAgent);
const navigatorAgent = navigator.userAgent;

function infoPopUp() {
  window.alert(
    `Your are using ${browserName},${OsName} with version ${version}, userAgent: ${navigatorAgent}`,
  );
}

infoPopUp();
