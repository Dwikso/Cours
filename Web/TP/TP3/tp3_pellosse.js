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

function codeSubstitution(msg, key) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let result = "";

  for (let i = 0; i < msg.length; i++) {
    let char = msg[i];
    if (char === " ") {
      result += " ";
    } else {
      let index = alphabet.indexOf(char);
      result += key[index];
    }
  }
  return result;
}

console.log(codeSubstitution("CECI EST UN TEST", "AZERTYUIOPQSDFGHJKLMWXCVBN"));

function decodeSubstitution(msg, key) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let result = "";
  for (let i = 0; i < msg.length; i++) {
    const char = msg[i];

    if (char === " ") {
      result += " ";
    } else {
      let index = key.indexOf(char);
      result += alphabet[index];
    }
  }

  return result;
}

console.log(
  decodeSubstitution("ETEO TLM WF MTLM", "AZERTYUIOPQSDFGHJKLMWXCVBN"),
);

console.log(
  decodeSubstitution('&"&! "¨ù `_ @`ù^" ù"¨ù', '@#&é"(§è!çà)-_$*€^¨ù`£=+:/'),
);
