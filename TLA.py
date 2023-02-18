# On va créer une la classe des graphes et leurs fonctionnalité ici

# On crée en premier les exeptions dont on aura besoin dans notre classe Gaphe

class StatAllReadyExist(Exception):
    pass

class TransiAllReadyExist(Exception):
    pass

class TransiDoesNotExist(Exception):
    pass

class TypeError(Exception):
    pass


class Graphe:
    def __init__(self, nom, alphabet = ["\0"], ens_etat = [], etat_init = [], etat_final = [], ens_transi = {}):
        self.nom = nom
        self.alphabet    = set(alphabet)
        self.ens_etat    = set(ens_etat)   or set()
        self.etat_init   = set(etat_init)  or set()
        self.etat_final  = set(etat_final) or set()
        self.ens_transi  = ens_transi
    
    def print_etat(self):
        if len(self.ens_etat) == 0:
            print('{}')
        else:
            print(self.ens_etat)
    
    def print_init(self):
        if len(self.etat_init) == 0:
            print('{}')
        else:
            print(self.etat_init)

    def print_final(self):
        if len(self.etat_final) == 0:
            print('{}')
        else:
            print(self.etat_final)
    
    def print_transi(self):
        print(f"#### enns transi de { self.nom } ####")
        if len(self.ens_transi) == 0:
            print('{}')
        else:
            for key in self.ens_transi.keys():
                print(f"{key}:")
                for transi in self.ens_transi[key]:
                    print(f"    {transi}")
        print('########')
    
    #gestion des états du graphe
    def add_etat(self, etat, spe = [None]):
        #on ajoute un état
        if etat in self.ens_etat:
            raise StatAllReadyExist()
        else:
            self.ens_etat.add(etat)
            self.ens_transi[etat] = []
            if "init" in spe:
                self.etat_init.add(etat)
            if "final" in spe:
                self.etat_final.add(etat)

    def add_init(self, etat):
        #on ajoute un état  inial si cet état est déjà dans l'ens des états
        if etat in self.ens_etat:
            self.etat_init.add(etat)
        else:
            self.add_etat(etat,["init"])


    def add_final(self, etat):
        #on ajoute un état
        if etat in self.ens_etat:
            self.etat_final.add(etat)
        else:
            self.add_etat(etat,["final"])

    def del_etat(self, etat):
        # pour supprimer un état on supprime cet état des différents ens d'états et on supprime tout les transi
        # qui vont vers ou qui partent de cet états
        if etat in self.ens_etat:
            self.ens_etat.remove(etat)
            if etat in self.etat_init:
                self.etat_init.remove(etat)
            if etat in self.etat_final:
                self.etat_final.remove(etat)
            self.ens_transi.pop(etat)    
            for transi in self.ens_transi:
                if etat in transi:
                    self.ens_transi.s

    # gestion des transi du graphe

    def add_transi(self,transi_label, etat_start, etat_end, double_sens = False):
        if (etat_start in self.ens_etat) and (etat_end in self.ens_etat):
            # on test si les deux états existe déjà bien
            print(f"{self.ens_transi[etat_start] = }")
            if tuple((etat_end,transi_label)) not in self.ens_transi[etat_start]:
                # on test si cette transition existe déjà
                if double_sens == False:
                    self.ens_transi[etat_start].append((etat_end, transi_label))
                else:
                    self.ens_transi[etat_start].append((etat_end, transi_label))
                    if tuple((etat_start,transi_label)) not in self.ens_transi[etat_end]:
                        self.ens_transi[etat_end].append((etat_start, transi_label))
            else:
                raise TransiAllReadyExist()
        else:
            raise StatAllReadyExist()
    
    def del_transi(self, transi_label, etat_start, etat_end):
        if [etat_start, transi_label, etat_end] in self.ens_transi:
            self.ens_transi.remove([etat_start, transi_label, etat_end])
        else:
            raise TransiDoesNotExist()




def is_determinist(graphe):
    if isinstance(graphe,Graphe):
        #on teste les 3 propri d un automate déterministe:
        # 1 seul état initail
        # Pas de transi ''
        # pas 2 transi du même nom qui parte du même état
        if len(graphe.etat_init) != 1:
            return False
        for key in graphe.ens_transi.keys():
            ens_label_transi = []
            for transi in graphe.ens_transi[key]:
                if transi[1] == '':
                    return False
                if transi in ens_label_transi:
                    return False
                else:
                    ens_label_transi.append(transi)
            if len(set(i[1] for i in ens_label_transi)) !=len(ens_label_transi):
                return False
        return True
    else:
        raise TypeError()

def ens_attainable(graphe, init):

    """
        gaphe  c'est un graphe
        init c est le point de départ 
        on va alors retourner tout les états que l'on peu atteindre à partir de l'état init
    """
    pile = [init]
    visit = []
    while len(pile) != 0:
        #on récup l'ensemble des transi qui partent du dernier élat de la pile
        etat_test = pile.pop()    #c est le bas de la pile qu on récupère
        print(etat_test)
        ens_transi_etat = graphe.ens_transi[etat_test]
        for transi in ens_transi_etat:
            #transi correspond a (etat_arrivé, label_de_la_transi)
            if transi[0] in visit:
                continue
            else:
                pile.append(transi[0])
        visit.append(etat_test)
    return visit

def dist_hamming(language_1, language_2):
    """
        prends en paramètre 2 languages et revoit la distance de Hamming
        entre ces 2 derniers
    """
    if isinstance(language_1, list) or isinstance(language_1, set):
        distance = max(len(i) for i in language_1)
        for mot_1 in language_1:
            for mot_2 in language_2:
                d = 0
                for ind_lettre in range(min(len(mot_1),len(mot_2))):
                    if mot_1[ind_lettre] != mot_2[ind_lettre]:
                        d += 1
                if d < distance:
                    distance = d
        return distance

def is_in_graphe_language(graphe, mot, init = None):
    """
        on met un para le graphe et un mot
        et on réalise un back-tracking sur le graphe pour déterminer
        si le mot est reconnue par l'automate
        on peut rajouter en paramètre un etat de départ 
        si init = None on utilise l'état initial pour commencer le traitement
    """
    if is_determinist(graphe):

        if init == None:
            #c'est une manière très moche de récupérer l'unique élément de
            #l'ensemble des états initiaux du graphe
            init = [ i for i in graphe.etat_init][0]
        # on prend en paramètre la longueur du mot que l'on va pouvoir décrémenter
        # jusqu'à ce qu'elle soit nulle dans le cas on le mot peut être lu

        pile = [ [ [init, ''] ] ]

        while pile:

            if pile[-1] == []:
                pile.pop()
            else:
                etat, mot_construit = pile[-1].pop()
                etat_suivant = []
                for etat_s in graphe.ens_transi[etat]:
                    if mot[0:len(mot_construit)+len(etat_s[1])] == mot_construit + etat_s[1]:
                        if (len(mot_construit+etat[1]) == len(mot)):
                            return True
                        etat_suivant.append([etat_s[0],mot_construit + etat_s[1]] )
                pile.append(etat_suivant)

        return False