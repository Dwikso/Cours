class Huffman:
    def __init__(self, data) -> None:
        self.data = data
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self._construire_tas()
        self._fusionner_noeuds()
        self._generer_codes()

    def _construire_tas(self):
        # Compter les fréquences manuellement
        frequences = {}
        for char in self.data:
            if char not in frequences:
                frequences[char] = 0
            frequences[char] += 1

        # Construire un tas manuellement
        for key, freq in frequences.items():
            self._inserer_tas((freq, key))

    def _inserer_tas(self, noeud):
        self.heap.append(noeud)
        self._remonter_tas(len(self.heap) - 1)

    def _extraire_tas(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        racine = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descendre_tas(0)
        return racine

    def _remonter_tas(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _descendre_tas(self, index):
        while True:
            enfant_gauche = 2 * index + 1
            enfant_droit = 2 * index + 2
            plus_petit = index

            if enfant_gauche < len(self.heap) and self.heap[enfant_gauche][0] < self.heap[plus_petit][0]:
                plus_petit = enfant_gauche
            if enfant_droit < len(self.heap) and self.heap[enfant_droit][0] < self.heap[plus_petit][0]:
                plus_petit = enfant_droit

            if plus_petit != index:
                self.heap[index], self.heap[plus_petit] = self.heap[plus_petit], self.heap[index]
                index = plus_petit
            else:
                break

    def _fusionner_noeuds(self):
        while len(self.heap) > 1:
            freq1, gauche = self._extraire_tas()
            freq2, droite = self._extraire_tas()
            fusion = freq1 + freq2
            self._inserer_tas((fusion, (gauche, droite)))

    def _generer_codes_helper(self, noeud, code_actuel):
        if isinstance(noeud, str):
            self.codes[noeud] = code_actuel
            self.reverse_mapping[code_actuel] = noeud
            return
        gauche, droite = noeud
        self._generer_codes_helper(gauche, code_actuel + "0")
        self._generer_codes_helper(droite, code_actuel + "1")

    def _generer_codes(self):
        racine = self._extraire_tas()[1]
        code_actuel = ""
        self._generer_codes_helper(racine, code_actuel)

    def obtenir_donnees_encodees(self):
        donnees_encodees = ""
        for char in self.data:
            donnees_encodees += self.codes[char]
        return donnees_encodees

    def decoder_donnees(self, donnees_encodees):
        code_actuel = ""
        donnees_decodees = ""
        for bit in donnees_encodees:
            code_actuel += bit
            if code_actuel in self.reverse_mapping:
                caractere = self.reverse_mapping[code_actuel]
                donnees_decodees += caractere
                code_actuel = ""
        return donnees_decodees
