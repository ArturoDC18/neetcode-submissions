class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counter = 0 
        answer = [0] * len(temperatures)
        pending = []
        to_remove = []
        for temp in temperatures:
            
            for pend in pending:
                if temp > pend[0]:
                    index = pend[1]
                    answer[index] = counter - index
                    print(f"Removed {pend} as {temp} > {pend[0]}, counter = {counter}")
                    to_remove.append(pend)
            for rem in to_remove:
                pending.remove(rem)
            to_remove = []

            tuple_o = (temp,counter)
            pending.append(tuple_o)
            print(f"Added {tuple_o}, pending = {pending}")
            counter += 1
        print(f"Returning answer with pending length = {len(pending)}")
        return answer
        