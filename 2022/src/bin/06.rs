use std::collections::HashSet;

// type opcode<'a> = (usize, &'a str);

fn get_opcodes(input: &str, len: usize) -> Vec<usize> {
    let mut ops: Vec<usize> = Vec::new();

    for i in len..input.len() {
        let op: Vec<char> = input[i-len..i].chars().collect();
        let setop: HashSet<char> = HashSet::from_iter(op.iter().copied());

        // println!("{len}: {i} {op:?}");

        if setop.len() == len {
            ops.push(i);
            // println!("\t pog");
        }
    }

    ops
}

pub fn part_one(input: &str) -> Option<u32> {
    let cringe = get_opcodes(input, 4);
    let first = *cringe.first().unwrap();

    Some(first as u32)
}

pub fn part_two(input: &str) -> Option<u32> {
    let cringe = get_opcodes(input, 14);
    let first = *cringe.first().unwrap();

    Some(first as u32)
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 6);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 6);
        assert_eq!(part_one(&input), Some(7));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 6);
        assert_eq!(part_two(&input), Some(19));
    }
}
