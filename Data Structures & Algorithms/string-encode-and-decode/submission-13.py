class Solution:
    # idea: use a special character to flag the division between each string
    # then, we can decode using the same string. Use append 

    #NEW IDEA: count the length of each string, append a list of numbers to 
    #indicate the cutoff

    def encode(self, strs: List[str]) -> str:
        output = ""
        lengths = ""

        #Empty case
        if len(strs) == 0:
            return "EMPTY"

        for string in strs: # account each string in list
            length = 0 # restart each string length
            for char in string:
                length += 1
            output += string
            lengths += str(length) + "#"
        return (lengths + "|" + output)


    def decode(self, s: str) -> List[str]:
        if s == "": return [""]
        if s == "EMPTY": return []
        output = []

        parts = s.split("|", 1)
        lengths_part = parts[0]
        words = parts[1] if len(parts) > 1 else ""
        
        to_decode = lengths_part.split("#")
        for length in to_decode:
            if length != "":
                l = int(length)
                output.append(words[:l])
                words = words[l:]

        return output
