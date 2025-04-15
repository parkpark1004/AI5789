#7.17

#(1)
population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 22, 4)
population_B = (308, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

votes_A = sum(population_A[2:])
votes_B = sum(population_B[2:])

print(f"마을 A와 B에 보낼 투표용지의 개수는 각각 {votes_A}장과 {votes_B}장입니다.")


#(2)
aging_A = sum(population_A[7:]) / sum(population_A)
aging_B = sum(population_B[7:]) / sum(population_B)

print(f"마을 A와 B의 고령화 정도는 각각 {aging_A:.3f}와 {aging_B:.3f}입니다.")
