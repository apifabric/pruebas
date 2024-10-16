import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLIERFRUIT_MODULE_DECLARATIONS, SupplierFruitRoutingModule} from  './SupplierFruit-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplierFruitRoutingModule
  ],
  declarations: SUPPLIERFRUIT_MODULE_DECLARATIONS,
  exports: SUPPLIERFRUIT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplierFruitModule { }