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
