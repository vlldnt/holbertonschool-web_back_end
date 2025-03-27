import Car from './10-car';

export default class EVcar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const newCar = new Car(this._brand, this._motor, this._color);
    return newCar;
  }
}
