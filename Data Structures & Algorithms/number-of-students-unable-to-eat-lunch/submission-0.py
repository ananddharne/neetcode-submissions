class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_preference = Counter(students)
        count_students = len(students)
        for sandwich in sandwiches:
            if count_preference[sandwich] > 0:
                count_students = count_students - 1
                count_preference[sandwich] = count_preference[sandwich] - 1
            else:
                return count_students
        
        return count_students



         


        