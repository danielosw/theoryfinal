class state:
	def __init__(self, transitions: list[tuple[str, str]]) -> None:
		self.transitions: list[tuple[str, str]] = transitions

	def transitionlookup(self, inputs: str) -> tuple[str, str] | bool:
		for i in self.transitions:
			if inputs.startswith(i[1]):
				return i
		return False


class dfa:
	def __init__(self, states: dict[str, state], symbols: list[str]) -> None:
		self.states: dict[str, state] = states
		self.symbols: list[str] = symbols

	def proccess(self, inputs: str, location: state, path: list[str]) -> tuple[bool, list[str]]:
		if inputs.__len__() == 0:
			return (True, path)
		transition = location.transitionlookup(inputs)
		if transition:
			path.append(transition[0])
			return self.proccess(
				inputs[transition[1].__len__() :], self.states[transition[0]], path
			)
		else:
			return (False, [])


def main() -> None:
	# create states
	S = state([("A", "http")])
	A = state([("B", "s://"), ("B", "://")])
	btransitions = [
		(x, y)
		for x, y in zip(
			["B" for _ in range(36)],
			[
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
			],
		)
	]
	btransitions.append(("C", "."))
	B = state(
		transitions=(btransitions),
	)
	C = state([("D", "com"), ("D", "edu"), ("D", "gov"), ("D", "mil"), ("D", "org"), ("D", "net")])
	D = state([])
	machine = dfa(
		{"S": S, "A": A, "B": B, "C": C, "D": D},
		[
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
			".",
		],
	)
	x, y = machine.proccess(input("Give string to proccess"), S, ["S"])
	if x:
		print("Succeeded with path: " + str(y))
	else:
		print("Failed")


if __name__ == "__main__":
	main()
