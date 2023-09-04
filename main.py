# write your code here
def padel_court_cost(court_type):

    if court_type == "indoor" :
        return 30
    elif court_type == "outdoor":
        return 20
    
def rackets_costs(racket_brand):

    if racket_brand == "bullpadel" :
      return 100
    elif racket_brand == "nox" :
        return 140
    elif racket_brand == "suix" :
        return 200
def padel_balls_costs(ball_boxes) :

    if ball_boxes == "box" :
        return 2
    elif ball_boxes == "two boxes" :
        return 3.5
    elif ball_boxes == "three boxes" :
        return 5 
    
def padel_game_cost():
        court_type = input("the court type")
        racket_brand =  input("racket brand")
        ball_boxes = input("number of ball boxes")

        total_costs =  padel_balls_costs(court_type)+ rackets_costs(racket_brand) + padel_balls_costs(ball_boxes
                                                                                                      )

        return total_costs 
total_costs = padel_game_cost()
print(f"""

total : {total_costs}

""")



       

         

       


    
          

    
    
