import {React, useState} from "react";
import Select from "react-select";


function ComboBox(props) {

    const [choice, setChoice] = useState('');

    const sendTargetCountry = () =>{
      props.getTargetCountry(choice)
  }

    const onChange = (value) => {
        setChoice(value)
    }

    const options = [
        { value: 'AED', label: 'United Arab Emirates' },
        { value: 'AUD', label: 'Australia' },
        { value: 'CAD', label: 'Canada' },
        { value: 'CNY', label: 'China' },
        { value: 'EUR', label: 'Europe' },
        { value: 'GBP', label: 'United Kingdom' },
        { value: 'HKD', label: 'Hong Kong' },
        { value: 'JPY_100', label: 'Japan' },
        { value: 'KRW', label: 'Korea' },
        { value: 'USD', label: 'United States' }
    ];

  return (
    <div className="App" style = {{fontSize : '1rem', color : '#000'}}>
      <Select
        defaultValue = {options[0]}
        options={options}
        value = {options.find(op => {
            return op.value === choice
        })}
        onChange={(value) => {
            onChange(value.value)
        }}
        openMenuOnClick = {sendTargetCountry()}
        />
    </div>
  );
}

export default ComboBox;