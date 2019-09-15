ScanPlan(bt,180,278.15,353.15,5)
sample_positions_2mmRack = {"water":56.8,"DIPA":61.6,"DIPA-H2O":66.1,"ECHA-H2O":83.5,
                       "ECHA":83.5,"DMCHA-H2O":95.9,"DMCHA":101.5,
                       "DPA-H2O":120.5,"DPA":125.2,"mt-kapton":135.0}

sample_index = {"water":??,"DIPA":??,"DIPA-H2O":??,"ECHA-H2O":??,
                       "ECHA":??,"DMCHA-H2O":??,"DMCHA":??,
                       "DPA-H2O":??,"DPA":??,"mt-kapton":??}

for sample, position in sample_positions_2mmRack.items():
    print(datetime.now())
    print("setting temperature to 5 C")
    cs700.set(278.15)
    print("temperature at {} K".format(cs700.position))
    print("moving to sample {} at position {} mm".format(sample,position))
    sample_x.move(position)
    print("arrived")
    print("starting Tramp")
    print(datetime.now())
    print("sanity check, read temperature: {} K".format(cs700.position))
    print("starting up scan")
    xrun(sample_index[sample],???(slow up))
    print("finished Tramp")
    print(datetime.now())
    print("starting fast down ramp")
    xrun(sample_index[sample],????(fast down))
