#!/bin/bash

# Get the list of projects
# ssh -p 29418 andrea-frittoli@review.openstack.org gerrit ls-projects > projects

# Clone them
# for ss in $(cat projects | grep openstack); do if [ ! -d $ss ]; then mkdir -p $ss; git clone https://git.openstack.org/$ss $ss; fi; done

cd ~/git/openstack
# Find the date on which plugin.sh was added those repos
for aa in $(find . -name plugin.sh | grep -v cookie | sed -n 's/^\([^ ]*\)\/devstack\/plugin\.sh/\1/p'); do
    echo "$(cd $aa; git log --diff-filter=A --format=%cd --date=short -1 -- devstack/plugin.sh) $(basename $aa)";
done | sort | awk '{ print $1" "NR" "$2 }' > devstack_plugins.dat

# Find the date on which upgrade.sh was added those repos
for aa in $(find . -name upgrade.sh | grep -v cookie | sed -n 's/^\([^ ]*\)\/devstack\/upgrade\/upgrade\.sh/\1/p'); do
    echo "$(cd $aa; git log --diff-filter=A --format=%cd --date=short -1 -- devstack/upgrade/upgrade.sh) $(basename $aa)";
done | sort | awk '{ print $1" "NR" "$2 }' > grenade_plugins.dat

# Find the date on which tempest plugin entry point was added
find . -name 'setup.cfg' -exec egrep -l '^tempest' '{}' \; | while read aa; do
    cd $(dirname $aa);
    echo "$(git blame -L '/^tempest/,+1' $(basename $aa) | awk '{print $1}' |xargs git log -1 --format=%cd --date=short) $(basename $(dirname $aa))";
    cd - &> /dev/null;
done | sort | awk '{ print $1" "NR" "$2 }' > tempest_plugins.dat
