import turtle


gens = 10
axiom = 'A'
chr_1, rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else rule_2 for chr in axiom])
