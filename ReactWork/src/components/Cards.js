import React from 'react';
import './Cards.css';
import CardItem from './CardItem';
import karachi from '../images/karachi.jpeg';
import lahore from '../images/lahore.jpeg';
import islamabad from '../images/islamabad.jpeg';
import peshawar from '../images/peshawar.jpeg';
import quetta from '../images/quetta.jpeg';


function Cards() {
  return (
    <div className='cards'>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src={karachi}
              text='The City of Lights.'
              label='Karachi'
            />
            <CardItem
              src={lahore}
              text='The city of cuisines.'
              label='Lahore'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src={islamabad}
              text='The Capital Territory.'
              label='Islamabad'
            />
            <CardItem
              src={peshawar}
              text='A land of rich culture.'
              label='Peshawar'
            />
            <CardItem
              src={quetta}
              text='City of delicacy.'
              label='Quetta'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;