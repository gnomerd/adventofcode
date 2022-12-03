use advent_of_code::helpers::parse_input;
use std::collections::HashSet;

static PRIORITY_CHARS: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn get_prio(c: char) -> u32 {
    let i = PRIORITY_CHARS.chars().position(|cc| cc == c).unwrap();
    i as u32 + 1
}

fn get_comps(row: &str) -> (HashSet<char>, HashSet<char>) {
    let (top, bot) = row.split_at(row.len() / 2);
    (
        HashSet::from_iter(top.chars()),
        HashSet::from_iter(bot.chars()),
    )
}

pub fn part_one(input: &str) -> Option<u32> {
    let comps = parse_input(input, get_comps);
    let intersections = comps.iter().map(|(t, b)| t.intersection(b));
    let priorities = intersections.map(|inters| inters.map(|c| get_prio(*c)));
    let sums: Vec<u32> = priorities.map(|inters| inters.sum()).collect();

    let sum: u32 = sums.iter().sum();

    Some(sum)
}

fn find_badge(group: &[&str]) -> char {
    let group_sets: Vec<HashSet<char>> = group
        .iter()
        .map(|s| HashSet::from_iter(s.chars()))
        .collect();

    let mut badges: HashSet<char> = group_sets[0]
        .intersection(&group_sets[1]) // cringe
        .copied()
        .collect();
    badges = badges.intersection(&group_sets[2]).copied().collect();

    *badges.iter().next().unwrap()
}

pub fn part_two(input: &str) -> Option<u32> {
    let lines: Vec<&str> = input.lines().collect();
    let groups = lines.chunks(3);

    let prios: Vec<u32> = groups.map(|group| get_prio(find_badge(group))).collect();

    let sum: u32 = prios.iter().sum();
    Some(sum)
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 3);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 3);
        assert_eq!(part_one(&input), Some(157));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 3);
        assert_eq!(part_two(&input), Some(70));
    }
}
