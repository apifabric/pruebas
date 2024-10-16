import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SALEDETAIL_MODULE_DECLARATIONS, SaleDetailRoutingModule} from  './SaleDetail-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SaleDetailRoutingModule
  ],
  declarations: SALEDETAIL_MODULE_DECLARATIONS,
  exports: SALEDETAIL_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SaleDetailModule { }