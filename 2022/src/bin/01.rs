fn parse_input(input: &str) -> Vec<u32> {
    // Split into each Elf
    let elves: Vec<&str> = input.split("\n\n").collect();

    // Map all the nums & sum
    elves
        .iter()
        .map(|s| s.lines().map(|n| n.parse::<u32>().unwrap()))
        .map(|nums| nums.sum::<u32>())
        .collect()
}

pub fn part_one(input: &str) -> Option<u32> {
    let cals = parse_input(input);
    cals.iter().max().copied()
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut cals = parse_input(input);
    cals.sort();
    cals.reverse();

    Some(cals[0..3].iter().sum())
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 1);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 1);
        assert_eq!(part_one(&input), Some(24000));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 1);
        assert_eq!(part_two(&input), Some(45000));
    }
}
