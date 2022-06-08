import Corruption
import Longest
import Shortest
import compute_Levenshtein_distanceDP

print("\tРозрахувати відстань Левенштейна:\n", compute_Levenshtein_distanceDP.my_dist("сова", "слова"))
print("\tЗнайти найдовший підрядок, який є спільним для рядків\n", Longest.Longest("сова", "слова"))
print("\tЗнайти Найменший підрядок, який є спільним для рядків\n", Shortest.Shortest("сова", "слова"))
print("\tГроші, які залишаться на аккаунті\n", Corruption.corruption(100, 2))


