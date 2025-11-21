import streamlit as st

def calculate_drops(measured_ppm, test_volume_ml, target_ppm, batch_volume_ml):
    if measured_ppm == 0:
        return 0
    ppm_per_drop_per_ml = measured_ppm / test_volume_ml
    ppm_per_drop_in_batch = ppm_per_drop_per_ml * batch_volume_ml
    return round(target_ppm / ppm_per_drop_in_batch, 2)

st.title("PPM Drop Calculator")

# Preset default volumes
default_batch_volume = 50.0
default_test_volume = 500.0

test_volume_ml = st.number_input("Volume used to test 1 drop (mL)", min_value=1.0, value=default_batch_volume)
batch_volume_ml = st.number_input("batch volume", min_value=1.0, value=default_test_volume)

minerals = ["Magnesium (Mg)", "Calcium (Ca)", "Sodium (Na)", "KHCO₃ (KH)"]

# Preset ppm defaults for each mineral (you can customize)
default_measured_ppm = {
    "Magnesium (Mg)": 145.0,
    "Calcium (Ca))": 245.0,
    "Sodium (Na)": 55.0,
    "KHCO₃ (KH)": 85.0
}

default_target_ppm = {
    "Magnesium (Mg)": 35.0,
    "Calcium (Ca)": 35.0,
    "Sodium (Na)": 10.0,
    "KHCO₃ (KH)": 10.0
}

st.header("Measured PPM of 1 drop in test volume")
measured_ppm = {}
for mineral in minerals:
    measured_ppm[mineral] = st.number_input(
        f"{mineral}",
        min_value=0.0,
        value=default_measured_ppm[mineral],
        key=f"measured_{mineral}"
    )

st.header("Target PPM in batch volume")
target_ppm = {}
for mineral in minerals:
    target_ppm[mineral] = st.number_input(
        f"{mineral}",
        min_value=0.0,
        value=default_target_ppm[mineral],
        key=f"target_{mineral}"
    )

if st.button("Calculate Drops Needed"):
    st.write("### Results:")
    for mineral in minerals:
        drops = calculate_drops(
            measured_ppm[mineral],
            batch_volume_ml,
            target_ppm[mineral],
            test_volume_ml
        )
        st.write(f"{mineral}: {drops} drops")


