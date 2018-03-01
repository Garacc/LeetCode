## LeetCode Summary

636. Exclusive Time of Functions: 栈

547. Friend Circles：DFS

655. Print Binary Tree：二叉树

221. Maximal Square：DP

85. Maximal Rectangle：单调栈(Histogram变形)

84. Largest Rectangle in Histogram：单调栈

463. Island Perimeter：简单对比(map+zip的使用) or 遍历查找

695. Max Area of Island：DFS(本来想用DP，发现出不来)

200. Number of Islands：DFS

731. My Calendar II：小空间匹配

729. My Calendar I：同上

*732. My Calendar III：难，小数据量可以用线段匹配，大数据量要用LCT(但是这东西看不懂)

606. Construct String from Binary Tree：中序遍历

127. Word Ladder：BFS，需要考虑wordlist的类型，如果是list会超时，所以需要选用set

*126. Word Ladder II：待完成

718. Maximum Length of Repeated Subarray：基本匹配

209. Minimum Size Subarray Sum：注意避免TLE

76. Minimum Window Substring：因为元素个数问题，不能用set

324. Wiggle Sort II：基于中间值的三段排序，或者直接排序

75. Sort Colors：/

71. Simplify Path：split和join的使用

5. Longest Palindromic Substring：和718不同，首先需要判断回文点

647. Palindromic Substrings：题目要求低，所以O(n2)的不会TLE，还是马拉车算法学习一个

214. Shortest Palindrome：easy game

516. Longest Palindromic Subsequence：DP

*730. Count Different Palindromic Subsequences：比较难的DP，需要重新做

135. Candy：很简单的一道算法题，一开始没想明白

122. Best Time to Buy and Sell Stock II：基础贪婪

121. Best Time to Buy and Sell Stock：Kadane算法（最大子序列和）

123. Best Time to Buy and Sell Stock III：DP

188. Best Time to Buy and Sell Stock IV：DP，需要判断交易次数和价格数量的大小关系，不然会爆内存

105. Construct Binary Tree from Preorder and Inorder Traversal：递归建树

106. Construct Binary Tree from Inorder and Postorder Traversal：同上

173. Binary Search Tree Iterator：题目描述不好，就是做一个inorder遍历

94. Binary Tree Inorder Traversal：递归

144. Binary Tree Preorder Traversal：同上

145. Binary Tree Postorder Traversal：同上

468. Validate IP Address：看起来很简单，但有很多坑

132. Palindrome Partitioning II：DP

131. Palindrome Partitioning：循环+递归

661. Image Smoother：算法很简单，但是各种极端情况都需要考虑

42. Trapping Rain Water：双指针

*407. Trapping Rain Water II：BFS

373. Find K Pairs with Smallest Sums：堆

378. Kth Smallest Element in a Sorted Matrix：bisect的灵活使用

*719. Find K-th Smallest Pair Distance：和378类似，但容易TLE，难

273. Integer to English Words：注意打表的拼写

12. Integer to Roman：暴力打表

13. Roman to Integer：判断低位字母的位置，标flag
