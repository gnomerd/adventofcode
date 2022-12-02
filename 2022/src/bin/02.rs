/*
 * -- 1 --
 * A = X = Rock
 * B = Y = Paper
 * C = Z = Scissors
 *
 * Rock > Scissors
 * Scissors > Paper
 * Paper > Rock
 *
 * -- 2 --
 * X = Lose
 * Y = Draw
 * Z = Win
 */

use advent_of_code::helpers::parse_input;

#[derive(Eq, PartialEq, Clone, Copy)]
enum RPS {
    R = 1,
    P = 2,
    S = 3,
}

enum State {
    W = 6,
    D = 3,
    L = 0,
}

fn map_ins(c: &str) -> RPS {
    match c {
        "A" | "X" => RPS::R,
        "B" | "Y" => RPS::P,
        "C" | "Z" => RPS::S,
        _ => panic!("Unknown operand: {}", c),
    }
}

fn offset(i: i32, len: usize) -> usize {
    ((i + len as i32) % len as i32) as usize
}

fn get_tactic_rps(opp: RPS, tactic: &str) -> RPS {
    let rps_range: [RPS; 3] = [RPS::R, RPS::P, RPS::S];

    let delta: i32 = match tactic {
        "X" => -1,
        "Y" => 0,
        "Z" => 1,
        _ => panic!("Unknown tactic operand {}", tactic),
    };
    let index = rps_range.iter().position(|&r| r == opp).unwrap();
    let i = offset(index as i32 + delta, rps_range.len());

    rps_range[i]
}

struct Round {
    opp: RPS,
    you: RPS,
}

impl Round {
    fn winner(&self) -> State {
        if self.opp == self.you {
            return State::D;
        }

        match (self.opp, self.you) {
            (RPS::S, RPS::R) => State::W,
            (RPS::P, RPS::S) => State::W,
            (RPS::R, RPS::P) => State::W,
            _ => State::L,
        }
    }

    fn score(&self) -> u32 {
        let state = self.winner() as u32;
        let rps = self.you as u32;
        rps + state
    }

    fn new(rnd: &str) -> Round {
        let splitted: Vec<&str> = rnd.split_whitespace().collect();
        let opp = map_ins(splitted[0]);
        let you = map_ins(splitted[1]);
        Round { opp, you }
    }

    fn new2(rnd: &str) -> Round {
        let splitted: Vec<&str> = rnd.split_whitespace().collect();
        let opp = map_ins(splitted[0]);
        let tactic = splitted[1];

        let you = get_tactic_rps(opp, tactic);

        Round { opp, you }
    }
}

pub fn part_one(input: &str) -> Option<u32> {
    let scores = parse_input(input, |r| Round::new(r).score());

    let score: u32 = scores.iter().sum();
    Some(score)
}

pub fn part_two(input: &str) -> Option<u32> {
    let scores = parse_input(input, |r| Round::new2(r).score());

    let score: u32 = scores.iter().sum();
    Some(score)
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 2);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 2);
        assert_eq!(part_one(&input), Some(15));
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 2);
        assert_eq!(part_two(&input), Some(12));
    }
}
