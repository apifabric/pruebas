import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Fruit-card.component.html',
  styleUrls: ['./Fruit-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Fruit-card]': 'true'
  }
})

export class FruitCardComponent {


}