import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'SupplierFruit-new',
  templateUrl: './SupplierFruit-new.component.html',
  styleUrls: ['./SupplierFruit-new.component.scss']
})
export class SupplierFruitNewComponent {
  @ViewChild("SupplierFruitForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}