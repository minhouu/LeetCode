class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
# horiziontally flipping
        for first_list in range(len(image)) :
            front = image[first_list][:len(image)//2]
            end = image[first_list][len(image)//2:]
            front.reverse()
            end.reverse()
            image[first_list] = end + front
# inverting        
        for first_list in range(len(image)) :
            for second_list in range(len(image)) :
                if image[first_list][second_list] == 1 :
                    image[first_list][second_list] = 0
                else :
                    image[first_list][second_list] = 1
        return image 