from TLA import *
a = Graphe('nom')

a.add_init('q_0')
a.add_etat('q_1')
a.add_etat('q_2')
a.add_etat('q_3')
a.add_etat('q_4')
a.add_final('q_5')

a.add_transi('a','q_0','q_1')
a.add_transi('a','q_2','q_4')

a.add_transi('b','q_1','q_2')

a.add_transi('c','q_2','q_1')
a.add_transi('c','q_0','q_2')
a.add_transi('c','q_3','q_5')

a.add_transi('bc','q_1','q_3')
a.add_transi('d','q_4','q_3')

a.add_transi('e','q_2','q_4')

a.print_transi()
print(is_determinist(a))

print(is_in_graphe_language(a, 'bcbedc','q_1'))