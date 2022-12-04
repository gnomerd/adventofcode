use advent_of_code::helpers::parse_input;
use std::collections::HashSet;

type Range = HashSet<u32>;

fn create_range(min: u32, max: u32) -> Range {
    let mut set: HashSet<u32> = HashSet::new();
    for i in min..max + 1 {
        set.insert(i);
    }

    set
}

fn from_str(txt: &str) -> Option<Range> {
    let mut nums = txt.split('-').map(|n| n.parse::<u32>());
    match (nums.next(), nums.next()) {
        (Some(Ok(min)), Some(Ok(max))) => Some(create_range(min, max)),

        _ => None,
    }
}

fn is_subsets(set_pair: &Vec<Range>) -> bool {
    let (first_set, second_set) = (&set_pair[0], &set_pair[1]);

    first_set.is_subset(second_set) || second_set.is_subset(first_set)
}

fn get_ranges_pairs(input: &str) -> Vec<Vec<Range>> {
    let rngs: Vec<Vec<Range>> = parse_input(input, |pair| {
        pair.split(',')
            .map(from_str)
            .map(|rng| rng.unwrap())
            .collect()
    });

    rngs
}

pub fn part_one(input: &str) -> Option<u32> {
    let rngs = get_ranges_pairs(input);
    let subsets: Vec<bool> = rngs.iter().map(is_subsets).collect();

    let count: usize = subsets.iter().filter(|&b| *b).count();

    Some(count as u32)
}

fn contains_at_all(set_pair: &Vec<Range>) -> bool {
    let (first_set, second_set) = (&set_pair[0], &set_pair[1]);

    let intersection: HashSet<u32> = first_set.intersection(second_set).copied().collect();

    !intersection.is_empty()
}

pub fn part_two(input: &str) -> Option<u32> {
    let rngs = get_ranges_pairs(input);
    let subsets: Vec<bool> = rngs.iter().map(contains_at_all).collect();

    let count: usize = subsets.iter().filter(|&b| *b).count();

    Some(count as u32)
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 4);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 4);
        assert_eq!(part_one(&input), Some(2));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 4);
        assert_eq!(part_two(&input), Some(4));
    }
}
