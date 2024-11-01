Висновки
Алгоритм DFS:

Обходить граф, заглиблюючись якомога далі по кожній гілці перед поверненням.
Може пропустити більш короткі шляхи, якщо вони знаходяться на сусідніх гілках.
Залежить від порядку обходу сусідів.
Алгоритм BFS:

Обходить граф пошарово, спочатку відвідуючи всіх сусідів поточного вузла.
Гарантовано знаходить найкоротший шлях за кількістю ребер в незваженому графі.
Менше залежить від порядку обходу, хоча він може впливати на конкретний маршрут серед рівноцінних за довжиною.
Практичне значення:

Для задач, де важливо знайти найкоротший шлях за мінімальною кількістю кроків (наприклад, у навігації або маршрутизації), краще використовувати BFS.
Якщо потрібно обійти всі можливі шляхи або знайти шлях до конкретної глибини, може бути корисним DFS.