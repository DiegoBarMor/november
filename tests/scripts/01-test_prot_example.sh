#!/bin/bash
set -eu

printf "TEST 01: PROT... "

start_time=$(date +%s)
output="$(python3 main.py prot tests/data/prot.pdb)"
end_time=$(date +%s)

expected="$(cat <<'EOF'
>>> Amber energies (NovemberFF) for 'tests/data/prot.pdb':
  BondEnergy: 530.5695854268687
  AngleEnergy: 1417.0459736853202
  DihedEnergy: 1558.1120122187128
  Nonbonded: -4111.194768700928
  ... LennardJones: -514.9366739454682
  ... Coulomb: -3596.2580947554598
EOF
)"

if [ "$output" != "$expected" ]; then
  printf "Output did not match expected.\n\n=== Output ===\n%s\n\n=== Expected ===\n%s\n" "$output" "$expected"
  exit 1
fi

printf "OK (%d seconds)\n" $((end_time - start_time))
