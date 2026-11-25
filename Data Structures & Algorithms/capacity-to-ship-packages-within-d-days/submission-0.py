class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Initialize the search space
        # Left_Ptr: Minimum possible ship capacity
        # Right_Ptr: Maximum possible ship capacity
        Left_Ptr, Right_Ptr = max(weights), sum(weights)

        while Left_Ptr <= Right_Ptr:
            # Candidate Ship Capacity
            min_weights_capacity = (Left_Ptr + Right_Ptr) // 2

            # Start with day 1 and an empty ship
            DAYS, TOTAL = 1, 0

            # Simulate shiping packages in order
            for weight in weights:
                if TOTAL + weight <= min_weights_capacity:
                    TOTAL += weight
                else:
                    # Start a new day
                    DAYS += 1
                    TOTAL = weight
            
            # check whether the capacity is sufficient
            if DAYS > days:
                # Increase the capacity
                Left_Ptr = min_weights_capacity + 1
            else:
                # The capacity works, let's decrease the capacity
                Right_Ptr = min_weights_capacity - 1

                
        # Return the minimum ship capacity
        return Left_Ptr
        
      
            

