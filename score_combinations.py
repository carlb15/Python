def num_score_combinations(score, safety, field_goal, touch_down):
  def helper(curr_score):
    if curr_score < 0:
      return 0
    elif curr_score == 0:
      return 1

    if max(A[curr_score][:]) == -1:
      A[0][curr_score] = helper(curr_score - safety)
      A[1][curr_score] = helper(curr_score - field_goal)
      A[2][curr_score] = helper(curr_score - touch_down)
  
    return max(A[curr_score][:])
  
  A = [[-1] * (score + 1) for _ in range(3)]

  return helper(score)
  
  
  
  
if __name__=="__main__":
  print(num_score_combinations(12, 2, 3, 7))