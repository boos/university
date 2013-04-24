import thread

class trails:
    """ Trails are updated at each interation of the alghorithm, 
        increasing the level of those related to moves that were part of 'good' solutions, 
        while decreasing all others. 

        After each iteration t of the algorithm, trails are updated
        using the following formula.

        τ ιψ (t ) = ρτιψ (t − 1) + ∆τ ιψ

        where ρ is a user-defined evaporation coefficient and
        ∆τιψ represents the sum of the contributions of all ants
        that used move (ιψ) to construct their solution.

        As iteration I mean after each set of ANTs have computed a solution.
        So at every algorithms interation first of all decrease all the value on the TRAILS. 
        Then for every ANT, increase the trails 
        For every ANT:
        - decrease first of all all the value of the TRAILS and th

        """

	# initialize a 3D matrix with all the moves of previous ANTs 
	def __init__(s, evaporation_coefficient, pherormone_constant):

        # create ADT for memorize trails 
		s.trails = dict()

        # Store evaporation coefficient of the pherormone 
        s.evaporation_coefficient = evaporation_coefficient

        # Store of how much every ANT increase pherormone trails when use a path 
        s.pherormone_constant = pherormone_constant 

        # create lock variable to handle access to critical sections 
		s.lock = thread.allocate_lock()


    def evaporation_action(s):
        """ Decrease globally all the trails """

		# start of critical section 
		s.lock.acquire()

        for x in trails:
            for y in trails[x]:
                for z in trails[x][y]:
                    trails[x][y][z] = s.evaporation_coefficient * trails[x][y][z] 

		# end of critical section
		s.lock.release()

    
	def update(s, selected_ant_moves):
		""" Increase trails used by single ANT 
            
            For every moves the ANT have done increase the trails on that path 
            Trails are increase with value of Q/L . 
            Q is a constant, L is the length of the complete solution """

        for selected_move in selected_ant_moves:

		    x = selected_move[0]
    		y = selected_move[1]
    		z = selected_move[2]

		# start of critical section 
		s.lock.acquire()

		if not s.trails.has_key(x):
			s.trails[x] = dict()

		if not s.trails[x].has_key(y):
			s.trails[x][y] = dict()

		if not s.trails[x][y].has_key(z):
			s.trails[x][y][z] = 0

        
		s.trails[x][y][z] = s.pherormone_constant / len (selected_ant_moves)

		s.lock.release()
		# end of critical section


	def value(s, selected_move)
		""" return trails value of a path """

		value = 0 

		x = selected_move[0]
		y = selected_move[1]
		z = selected_move[2]

		s.lock.acquire()

		# start of critical section 
		if s.trails.has_key(x) and s.trails[x].has_ke(y) and s.trails[x][y].has_key(z):
			value = s.trails[x][y][z]

		s.lock.release()
		# end of critical secion 

		return value
