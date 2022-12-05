use advent_of_code::helpers::transpose;
use regex::Regex;

type Stack = Vec<char>;

fn split_input(input: &str) -> (&str, &str) {
    let splitted: Vec<&str> = input.split("\n\n").collect();

    (splitted[0], splitted[1])
}

fn build_stack(stack_str: &str) -> Stack {
    let stack_regex_builder = Regex::new(r"[A-Z]").unwrap();
    let matches: Vec<&str> = stack_regex_builder
        .find_iter(stack_str)
        .map(|m| m.as_str())
        .collect();

    let mut stack = Stack::new();
    for cr in matches[0..].iter() {
        stack.push(cr.chars().next().unwrap());
    }

    stack
}

fn create_stacks(stack_input: &str) -> Vec<Stack> {
    let lines: Vec<Vec<char>> = stack_input
        .lines()
        .map(|txt| txt.chars().collect::<Vec<char>>())
        .map(|line| format!("{:>10}", line.iter().collect::<String>()))
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    let transpose_regex_filter = Regex::new(r"[A-Z]+\d+").unwrap();

    let transposed_lines: Vec<String> = transpose(lines)
        .iter()
        .map(String::from_iter)
        .filter(|s| transpose_regex_filter.is_match(s))
        .map(|s| s.chars().rev().collect())
        .collect();

    let stacks: Vec<&str> = transposed_lines.iter().map(|s| s.trim()).collect();

    let stacks: Vec<Stack> = stacks.iter().map(|s| build_stack(s)).collect();

    stacks
}

fn parse_ins(ins: &str) -> (u32, u32, u32) {
    let opcode_regex = Regex::new(r"\d+").unwrap();
    let opcodes: Vec<u32> = opcode_regex
        .find_iter(ins)
        .map(|m| m.as_str())
        .map(|s| s.parse::<u32>().unwrap())
        .collect();

    (opcodes[0], opcodes[1] - 1, opcodes[2] - 1)
}

fn perform_ins(stacks: &mut Vec<Stack>, ins: &str) {
    let (amount, src, dest) = parse_ins(ins);

    for _ in 0..amount {
        let transfer_value = stacks[src as usize].pop().unwrap();
        stacks[dest as usize].push(transfer_value);
    }
}

pub fn part_one(input: &str) -> Option<String> {
    let (stack_input, instructions_input) = split_input(input);

    let mut stacks = create_stacks(stack_input);

    for ins in instructions_input.lines() {
        perform_ins(&mut stacks, ins);
    }

    let tops: Vec<char> = stacks
        .iter()
        .map(|stack| *stack.last().unwrap_or(&' '))
        .collect();

    let output: String = tops.iter().collect();

    Some(output)
}

fn perform_ins_9001(stacks: &mut Vec<Stack>, ins: &str) {
    let (amount, src, dest) = parse_ins(ins);

    let mut cont_buffer: Vec<char> = Vec::new();
    for _ in 0..amount {
        let transfer_value = stacks[src as usize].pop().unwrap();
        cont_buffer.push(transfer_value);
    }

    cont_buffer.reverse();
    stacks[dest as usize].append(&mut cont_buffer);
}

pub fn part_two(input: &str) -> Option<String> {
    let (stack_input, instructions_input) = split_input(input);

    let mut stacks = create_stacks(stack_input);

    for ins in instructions_input.lines() {
        perform_ins_9001(&mut stacks, ins);
    }

    let tops: Vec<char> = stacks
        .iter()
        .map(|stack| *stack.last().unwrap_or(&' '))
        .collect();

    let output: String = tops.iter().collect();

    Some(output)
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 5); // inputs
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 5);
        assert_eq!(part_one(&input), Some(String::from("CMZ")));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 5);
        assert_eq!(part_two(&input), Some(String::from("MCD")));
    }
}
