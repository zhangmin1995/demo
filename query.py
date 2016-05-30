SELECT * 
    FROM hw_b as b
    WHERE b.sn not in
        (SELECT sn
             FROM hw_a);
b.commit();

