class state:
	# simple init, transitions are a list of tuple's of (x,y) where x is the destination and y is that is required for it
	def __init__(self, transitions: list[tuple[str, str]]) -> None:
		self.transitions: list[tuple[str, str]] = transitions

	# lookup of their are any transitions that execept this value and returns the first one that does
	# this means that more specific transitions need to be first in the list, and it does not work with non-determinism
	def transitionlookup(self, inputs: str) -> tuple[str, str] | bool:
		for i in self.transitions:
			if inputs.startswith(i[1]):
				return i
		return False


class dfa:
	# simple init, states are a dict where the string is the name of the state, and it matches to the object
	def __init__(self, states: dict[str, state], symbols: list[str]) -> None:
		self.states: dict[str, state] = states
		self.symbols: list[str] = symbols

	# proccess the string and return a tuple of if it succseded and if it did the path it took
	def proccess(
		self, inputs: str, location: state, path: list[tuple[str, str]], current: str
	) -> tuple[bool, list[tuple[str, str]]]:
		# if the input is empty return true and the path
		# base case
		if inputs.__len__() == 0:
			return (True, path)
		# lookup a valid trasition
		transition = location.transitionlookup(inputs)
		# if their is one
		if transition:
			# add the node we are in, and what we consumed
			path.append((current, transition[1]))
			# recurse, cosuming what trasition needs from inputs and setting the location to our new node
			return self.proccess(
				inputs[transition[1].__len__() :], self.states[transition[0]], path, transition[0]
			)
		else:
			# if thier is not a valid trasistion then this is not in the language
			return (False, [])


# A is machine, w is string, S is the start state
def accept(A: dfa, w: str, S: state) -> tuple[bool, list[tuple[str, str]]]:
	return A.proccess(w, S, [], "S")


def main() -> None:
	# create states
	S = state([("A", "http")])
	A = state([("B", "s://"), ("B", "://")])
	alphabetExceptPeriod: list[str] = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
	alphabetExceptPeriodOld: list[str] = [
		"a",
		"b",
		"c",
		"d",
		"e",
		"f",
		"g",
		"h",
		"i",
		"j",
		"k",
		"l",
		"m",
		"n",
		"o",
		"p",
		"q",
		"r",
		"s",
		"t",
		"u",
		"v",
		"w",
		"x",
		"y",
		"z",
		"0",
		"1",
		"2",
		"3",
		"4",
		"5",
		"6",
		"7",
		"8",
		"9",
	]
	# I rewrote to make it easier to read but incase they are not equivelent we do this
	if alphabetExceptPeriod != alphabetExceptPeriodOld:
		alphabetExceptPeriod = alphabetExceptPeriodOld
	btransitions = [
		(x, y)
		for x, y in zip(
			["B" for _ in range(36)],
			alphabetExceptPeriod,
		)
	] + [("C", ".")]
	B = state(
		transitions=(btransitions),
	)
	C = state([("D", "com"), ("D", "edu"), ("D", "gov"), ("D", "mil"), ("D", "org"), ("D", "net")])
	D = state([])
	# load the states
	machine = dfa(
		{"S": S, "A": A, "B": B, "C": C, "D": D},
		[*alphabetExceptPeriod, ".", ":"],
	)
	x, y = accept(machine, input("Give string to proccess: "), S)
	if x:
		print("Accepted: " + str(y))
	else:
		print("Rejected")


if __name__ == "__main__":
	main()
