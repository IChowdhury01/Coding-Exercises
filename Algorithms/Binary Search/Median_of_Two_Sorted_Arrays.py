class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            m = l + (r-l)//2
            m2 = half - (m+1) - 1

            Aleft = float('-inf') if m < 0 else A[m]
            Aright = float('inf') if m+1 >= len(A) else A[m+1]
            Bleft = float('-inf') if m2 < 0 else B[m2]
            Bright = float('inf') if m2+1 >= len(B) else B[m2+1]

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                # Make Aleft smaller
                r = m - 1
            else:
                l = m + 1
