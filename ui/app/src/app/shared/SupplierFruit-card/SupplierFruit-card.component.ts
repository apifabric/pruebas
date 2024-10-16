import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SupplierFruit-card.component.html',
  styleUrls: ['./SupplierFruit-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SupplierFruit-card]': 'true'
  }
})

export class SupplierFruitCardComponent {


}