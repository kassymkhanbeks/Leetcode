# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for i in range(len(s)):
			if s[i] == '(' or s[i] == '{' or s[i] == '[':
				stack.append(s[i])
			else:
				if len(stack) == 0:
					return False
				c = stack.pop()
				if not ((s[i] == ')' and c == '(') or
						(s[i] == '}' and c == '{') or
						(s[i] == ']' and c == '[')):
					return False

		return len(stack) == 0

# leetcode submit region end(Prohibit modification and deletion)
