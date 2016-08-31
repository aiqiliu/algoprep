# 388. Longest Absolute File Path
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        m = len(input)
        if m == 0 or "." not in input:
            return 0
        
        cp_input = input.split("\n")
        max_len = 0
     
        if "." in cp_input[0]:
            max_len = len(cp_input[0])
            return max_len

        for index in range(0, len(cp_input)):
            curr = cp_input[index]
            if "." in curr:
                length = 0
                valid = curr.count("\t")
                pointer = index - 1
                length += len(curr) - valid 
                
                while valid >= 0 and pointer >= 0:
                    if cp_input[pointer].count("\t") == valid - 1:
                        valid -= 1
                        length += len(cp_input[pointer]) - valid + 1

                    pointer -= 1
                
                if length > max_len:
                    max_len = length
               
        return max_len