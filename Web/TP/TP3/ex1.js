function valAbslue(x) {
  if (x < 0) {
    return -x;
  } else {
    return x;
  }
}

function CodeCesar(msg, key) {
  let result = "";
  for (let i = 0; i < msg.length; i++) {
    let char = msg[i].toUpperCase().charCodeAt();
    char += valAbslue(key);
    if (char >= 90) {
      char -= 26;
    }
    result += String.fromCharCode(char);
  }
  return result;
}

console.log(CodeCesar("zorro", 3));

function decodeCodeCesar(msg, key) {
  let result = "";
  for (let i = 0; i < msg.length; i++) {
    let char = msg[i].toUpperCase().charCodeAt();
    char -= valAbslue(key);
    if (char <= 65) {
      char += 26;
    }
    result += String.fromCharCode(char);
  }
  return result;
}

console.log(decodeCodeCesar("cruur", 3));

function CodeCesar2(msg, key) {
  let result = "";
  for (let i = 0; i < msg.length; i++) {
    if (msg[i] !== " ") {
      let char = msg[i].charCodeAt();
      char += key;
      result += String.fromCharCode(char);
    } else {
      result += " ";
    }
  }
  return result;
}

console.log(CodeCesar2("COUCOU TOUT LE MONDE", 3));

function CodeCesar3(msg, key, blanks) {
  let result = "";
  for (let i = 0; i < msg.length; i++) {
    if (blanks.includes(msg[i]) || msg[i] === " ") {
      result += msg[i];
    } else {
      let char = msg[i].charCodeAt();
      char += key;
      result += String.fromCharCode(char);
    }
  }
  return result;
}

console.log(CodeCesar3("COUCOU, TOUT LE MONDE !", 3, ", !"));
