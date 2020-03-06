#### The Law Firm Pratt and Roberts
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'jahseh onfroy' # Only 10 chars displayed.
strategy_name = 'ganggang'
strategy_description = "odds and evens"

import random   
def move(my_history,their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
   #  gamecnt = len(their_history)
   #  betrayflag = False
   #  if len(my_history)==0: # It's the first round; collude.
   #      return 'c'
   #  while gamecnt>0:
   #      if their_history[gamecnt] == 'b':
   #          return 'b'
   #      gamecnt -= 1
   # 
   #  return 'c'
    if len(my_history)==0: # It's the first round; collude.
        return 'c'    
    else:
        #if random number is even, return c otherwise return b
        a = random.randint(1,10)
        if a % 2 == 0:
            return 'c'
        else: 
            return 'b'
        
       
  
        

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'